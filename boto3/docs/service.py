# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from botocore.exceptions import DataNotFoundError
from botocore.docs.paginator import PaginatorDocumenter
from botocore.docs.waiter import WaiterDocumenter
from botocore.docs.bcdoc.restdoc import DocumentStructure

from boto3.docs.client import Boto3ClientDocumenter
from boto3.docs.resource import ResourceDocumenter
from boto3.docs.resource import ServiceResourceDocumenter


class ServiceDocumenter(object):
    def __init__(self, service_name, session):
        self._service_name = service_name
        self._session = session
        # I know that this is an internal attribute, but the botocore session
        # is needed to load the paginator and waiter models.
        self._botocore_session = session._session
        self._client = self._session.client(service_name)
        self._service_resource = None
        if self._service_name in self._session.get_available_resources():
            self._service_resource = self._session.resource(service_name)
        self.sections = [
            'title',
            'table-of-contents',
            'client',
            'paginators',
            'waiters',
            'service-resource',
            'resources'
        ]

    def document_service(self):
        """Documents an entire service.

        :returns: The reStructured text of the documented service.
        """
        doc_structure = DocumentStructure(
            self._service_name, section_names=self.sections,
            target='html')
        self._document_title(doc_structure.get_section('title'))
        self._document_table_of_contents(
            doc_structure.get_section('table-of-contents'))
        self._document_client(doc_structure.get_section('client'))
        self._document_paginators(doc_structure.get_section('paginators'))
        self._document_waiters(doc_structure.get_section('waiters'))
        if self._service_resource:
            self._document_service_resource(
                doc_structure.get_section('service-resource'))
            self._document_resources(doc_structure.get_section('resources'))
        return doc_structure.flush_structure()

    def _document_title(self, section):
        section.style.h1(self._client.__class__.__name__)

    def _document_table_of_contents(self, section):
        section.style.table_of_contents(title='Table of Contents', depth=2)

    def _document_client(self, section):
        Boto3ClientDocumenter(self._client).document_client(section)

    def _document_paginators(self, section):
        try:
            paginator_model = self._botocore_session.get_paginator_model(
                self._service_name)
        except DataNotFoundError:
            return
        paginator_documenter = PaginatorDocumenter(
            self._client, paginator_model)
        paginator_documenter.document_paginators(section)

    def _document_waiters(self, section):
        if self._client.waiter_names:
            service_waiter_model = self._botocore_session.get_waiter_model(
                self._service_name)
            waiter_documenter = WaiterDocumenter(
                self._client, service_waiter_model)
            waiter_documenter.document_waiters(section)

    def _document_service_resource(self, section):
        ServiceResourceDocumenter(
            self._service_resource, self._botocore_session).document_resource(
                section)

    def _document_resources(self, section):
        temp_identifier_value = 'foo'
        loader = self._botocore_session.get_component('data_loader')
        json_resource_model = loader.load_service_model(
            self._service_name, 'resources-1')
        for resource_name in json_resource_model['resources']:
            resource_model = json_resource_model['resources'][resource_name]
            resource_cls = self._session.resource_factory.load_from_definition(
                service_name=self._service_name,
                resource_name=resource_name,
                model=resource_model,
                resource_defs=json_resource_model['resources'],
                service_model=self._service_resource.meta.
                client.meta.service_model
            )
            identifiers = resource_cls.meta.resource_model.identifiers
            args = []
            for _ in identifiers:
                args.append(temp_identifier_value)
            resource = resource_cls(*args, client=self._client)
            ResourceDocumenter(
                resource, self._botocore_session).document_resource(
                    section.add_new_section(resource.meta.resource_model.name))
