

*******
Route53
*******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Route53.Client

  A low-level client representing Amazon Route 53::

    
    import boto3
    
    client = boto3.client('route53')

  
  These are the available methods:
  
  *   :py:meth:`~Route53.Client.associate_vpc_with_hosted_zone`

  
  *   :py:meth:`~Route53.Client.can_paginate`

  
  *   :py:meth:`~Route53.Client.change_resource_record_sets`

  
  *   :py:meth:`~Route53.Client.change_tags_for_resource`

  
  *   :py:meth:`~Route53.Client.create_health_check`

  
  *   :py:meth:`~Route53.Client.create_hosted_zone`

  
  *   :py:meth:`~Route53.Client.create_query_logging_config`

  
  *   :py:meth:`~Route53.Client.create_reusable_delegation_set`

  
  *   :py:meth:`~Route53.Client.create_traffic_policy`

  
  *   :py:meth:`~Route53.Client.create_traffic_policy_instance`

  
  *   :py:meth:`~Route53.Client.create_traffic_policy_version`

  
  *   :py:meth:`~Route53.Client.create_vpc_association_authorization`

  
  *   :py:meth:`~Route53.Client.delete_health_check`

  
  *   :py:meth:`~Route53.Client.delete_hosted_zone`

  
  *   :py:meth:`~Route53.Client.delete_query_logging_config`

  
  *   :py:meth:`~Route53.Client.delete_reusable_delegation_set`

  
  *   :py:meth:`~Route53.Client.delete_traffic_policy`

  
  *   :py:meth:`~Route53.Client.delete_traffic_policy_instance`

  
  *   :py:meth:`~Route53.Client.delete_vpc_association_authorization`

  
  *   :py:meth:`~Route53.Client.disassociate_vpc_from_hosted_zone`

  
  *   :py:meth:`~Route53.Client.generate_presigned_url`

  
  *   :py:meth:`~Route53.Client.get_account_limit`

  
  *   :py:meth:`~Route53.Client.get_change`

  
  *   :py:meth:`~Route53.Client.get_checker_ip_ranges`

  
  *   :py:meth:`~Route53.Client.get_geo_location`

  
  *   :py:meth:`~Route53.Client.get_health_check`

  
  *   :py:meth:`~Route53.Client.get_health_check_count`

  
  *   :py:meth:`~Route53.Client.get_health_check_last_failure_reason`

  
  *   :py:meth:`~Route53.Client.get_health_check_status`

  
  *   :py:meth:`~Route53.Client.get_hosted_zone`

  
  *   :py:meth:`~Route53.Client.get_hosted_zone_count`

  
  *   :py:meth:`~Route53.Client.get_hosted_zone_limit`

  
  *   :py:meth:`~Route53.Client.get_paginator`

  
  *   :py:meth:`~Route53.Client.get_query_logging_config`

  
  *   :py:meth:`~Route53.Client.get_reusable_delegation_set`

  
  *   :py:meth:`~Route53.Client.get_reusable_delegation_set_limit`

  
  *   :py:meth:`~Route53.Client.get_traffic_policy`

  
  *   :py:meth:`~Route53.Client.get_traffic_policy_instance`

  
  *   :py:meth:`~Route53.Client.get_traffic_policy_instance_count`

  
  *   :py:meth:`~Route53.Client.get_waiter`

  
  *   :py:meth:`~Route53.Client.list_geo_locations`

  
  *   :py:meth:`~Route53.Client.list_health_checks`

  
  *   :py:meth:`~Route53.Client.list_hosted_zones`

  
  *   :py:meth:`~Route53.Client.list_hosted_zones_by_name`

  
  *   :py:meth:`~Route53.Client.list_query_logging_configs`

  
  *   :py:meth:`~Route53.Client.list_resource_record_sets`

  
  *   :py:meth:`~Route53.Client.list_reusable_delegation_sets`

  
  *   :py:meth:`~Route53.Client.list_tags_for_resource`

  
  *   :py:meth:`~Route53.Client.list_tags_for_resources`

  
  *   :py:meth:`~Route53.Client.list_traffic_policies`

  
  *   :py:meth:`~Route53.Client.list_traffic_policy_instances`

  
  *   :py:meth:`~Route53.Client.list_traffic_policy_instances_by_hosted_zone`

  
  *   :py:meth:`~Route53.Client.list_traffic_policy_instances_by_policy`

  
  *   :py:meth:`~Route53.Client.list_traffic_policy_versions`

  
  *   :py:meth:`~Route53.Client.list_vpc_association_authorizations`

  
  *   :py:meth:`~Route53.Client.test_dns_answer`

  
  *   :py:meth:`~Route53.Client.update_health_check`

  
  *   :py:meth:`~Route53.Client.update_hosted_zone_comment`

  
  *   :py:meth:`~Route53.Client.update_traffic_policy_comment`

  
  *   :py:meth:`~Route53.Client.update_traffic_policy_instance`

  

  .. py:method:: associate_vpc_with_hosted_zone(**kwargs)

    

    Associates an Amazon VPC with a private hosted zone. 

     

    .. warning::

       

      To perform the association, the VPC and the private hosted zone must already exist. You can't convert a public hosted zone into a private hosted zone.

       

     

    .. note::

       

      If you want to associate a VPC that was created by using one AWS account with a private hosted zone that was created by using a different account, the AWS account that created the private hosted zone must first submit a ``CreateVPCAssociationAuthorization`` request. Then the account that created the VPC must submit an ``AssociateVPCWithHostedZone`` request.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/AssociateVPCWithHostedZone>`_    


    **Request Syntax** 
    ::

      response = client.associate_vpc_with_hosted_zone(
          HostedZoneId='string',
          VPC={
              'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
              'VPCId': 'string'
          },
          Comment='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the private hosted zone that you want to associate an Amazon VPC with.

       

      Note that you can't associate a VPC with a hosted zone that doesn't have an existing VPC association.

      

    
    :type VPC: dict
    :param VPC: **[REQUIRED]** 

      A complex type that contains information about the VPC that you want to associate with a private hosted zone.

      

    
      - **VPCRegion** *(string) --* 

        (Private hosted zones only) The region in which you created an Amazon VPC.

        

      
      - **VPCId** *(string) --* 

        (Private hosted zones only) The ID of an Amazon VPC. 

        

      
    
    :type Comment: string
    :param Comment: 

       *Optional:* A comment about the association request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the ``AssociateVPCWithHostedZone`` request.

        
        

        - **ChangeInfo** *(dict) --* 

          A complex type that describes the changes made to your hosted zone.

          
          

          - **Id** *(string) --* 

            The ID of the request.

            
          

          - **Status** *(string) --* 

            The current state of the request. ``PENDING`` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

            
          

          - **SubmittedAt** *(datetime) --* 

            The date and time that the change request was submitted in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

            
          

          - **Comment** *(string) --* 

            A complex type that describes change information about changes made to your hosted zone.

             

            This element contains an ID that you use when performing a  GetChange action to get detailed information about the change.

            
      
    

  .. py:method:: can_paginate(operation_name)

        
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name.  This is the same name
        as the method name on the client.  For example, if the
        method name is ``create_foo``, and you'd normally invoke the
        operation as ``client.create_foo(**kwargs)``, if the
        ``create_foo`` operation can be paginated, you can use the
        call ``client.get_paginator("create_foo")``.
    
    :return: ``True`` if the operation can be paginated,
        ``False`` otherwise.


  .. py:method:: change_resource_record_sets(**kwargs)

    

    Creates, changes, or deletes a resource record set, which contains authoritative DNS information for a specified domain name or subdomain name. For example, you can use ``ChangeResourceRecordSets`` to create a resource record set that routes traffic for test.example.com to a web server that has an IP address of 192.0.2.44.

     

     **Change Batches and Transactional Changes**  

     

    The request body must include a document with a ``ChangeResourceRecordSetsRequest`` element. The request body contains a list of change items, known as a change batch. Change batches are considered transactional changes. When using the Amazon Route 53 API to change resource record sets, Amazon Route 53 either makes all or none of the changes in a change batch request. This ensures that Amazon Route 53 never partially implements the intended changes to the resource record sets in a hosted zone. 

     

    For example, a change batch request that deletes the ``CNAME`` record for www.example.com and creates an alias resource record set for www.example.com. Amazon Route 53 deletes the first resource record set and creates the second resource record set in a single operation. If either the ``DELETE`` or the ``CREATE`` action fails, then both changes (plus any other changes in the batch) fail, and the original ``CNAME`` record continues to exist.

     

    .. warning::

       

      Due to the nature of transactional changes, you can't delete the same resource record set more than once in a single change batch. If you attempt to delete the same change batch more than once, Amazon Route 53 returns an ``InvalidChangeBatch`` error.

       

     

     **Traffic Flow**  

     

    To create resource record sets for complex routing configurations, use either the traffic flow visual editor in the Amazon Route 53 console or the API actions for traffic policies and traffic policy instances. Save the configuration as a traffic policy, then associate the traffic policy with one or more domain names (such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in multiple hosted zones. You can roll back the updates if the new configuration isn't performing as expected. For more information, see `Using Traffic Flow to Route DNS Traffic <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html>`__ in the *Amazon Route 53 Developer Guide* .

     

     **Create, Delete, and Upsert**  

     

    Use ``ChangeResourceRecordsSetsRequest`` to perform the following actions:

     

     
    * ``CREATE`` : Creates a resource record set that has the specified values. 
     
    * ``DELETE`` : Deletes an existing resource record set that has the specified values. 
     
    * ``UPSERT`` : If a resource record set does not already exist, AWS creates it. If a resource set does exist, Amazon Route 53 updates it with the values in the request.  
     

     

     **Syntaxes for Creating, Updating, and Deleting Resource Record Sets**  

     

    The syntax for a request depends on the type of resource record set that you want to create, delete, or update, such as weighted, alias, or failover. The XML elements in your request must appear in the order listed in the syntax. 

     

    For an example for each type of resource record set, see "Examples."

     

    Don't refer to the syntax in the "Parameter Syntax" section, which includes all of the elements for every kind of resource record set that you can create, delete, or update by using ``ChangeResourceRecordSets`` . 

     

     **Change Propagation to Amazon Route 53 DNS Servers**  

     

    When you submit a ``ChangeResourceRecordSets`` request, Amazon Route 53 propagates your changes to all of the Amazon Route 53 authoritative DNS servers. While your changes are propagating, ``GetChange`` returns a status of ``PENDING`` . When propagation is complete, ``GetChange`` returns a status of ``INSYNC`` . Changes generally propagate to all Amazon Route 53 name servers within 60 seconds. For more information, see  GetChange .

     

     **Limits on ChangeResourceRecordSets Requests**  

     

    For information about the limits on a ``ChangeResourceRecordSets`` request, see `Limits <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html>`__ in the *Amazon Route 53 Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ChangeResourceRecordSets>`_    


    **Request Syntax** 
    ::

      response = client.change_resource_record_sets(
          HostedZoneId='string',
          ChangeBatch={
              'Comment': 'string',
              'Changes': [
                  {
                      'Action': 'CREATE'|'DELETE'|'UPSERT',
                      'ResourceRecordSet': {
                          'Name': 'string',
                          'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                          'SetIdentifier': 'string',
                          'Weight': 123,
                          'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                          'GeoLocation': {
                              'ContinentCode': 'string',
                              'CountryCode': 'string',
                              'SubdivisionCode': 'string'
                          },
                          'Failover': 'PRIMARY'|'SECONDARY',
                          'MultiValueAnswer': True|False,
                          'TTL': 123,
                          'ResourceRecords': [
                              {
                                  'Value': 'string'
                              },
                          ],
                          'AliasTarget': {
                              'HostedZoneId': 'string',
                              'DNSName': 'string',
                              'EvaluateTargetHealth': True|False
                          },
                          'HealthCheckId': 'string',
                          'TrafficPolicyInstanceId': 'string'
                      }
                  },
              ]
          }
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone that contains the resource record sets that you want to change.

      

    
    :type ChangeBatch: dict
    :param ChangeBatch: **[REQUIRED]** 

      A complex type that contains an optional comment and the ``Changes`` element.

      

    
      - **Comment** *(string) --* 

         *Optional:* Any comments you want to include about a change batch request.

        

      
      - **Changes** *(list) --* **[REQUIRED]** 

        Information about the changes to make to the record sets.

        

      
        - *(dict) --* 

          The information for each resource record set that you want to change.

          

        
          - **Action** *(string) --* **[REQUIRED]** 

            The action to perform:

             

             
            * ``CREATE`` : Creates a resource record set that has the specified values. 
             
            * ``DELETE`` : Deletes a existing resource record set. 

            .. warning::

               To delete the resource record set that is associated with a traffic policy instance, use ``  DeleteTrafficPolicyInstance `` . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ``ChangeResourceRecordSets`` , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use.  

             
             
            * ``UPSERT`` : If a resource record set doesn't already exist, Amazon Route 53 creates it. If a resource record set does exist, Amazon Route 53 updates it with the values in the request. 
             

            

          
          - **ResourceRecordSet** *(dict) --* **[REQUIRED]** 

            Information about the resource record set to create, delete, or update.

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the domain you want to perform the action on.

               

              Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical.

               

              For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following:

               

               
              * The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` . 
               
              * The * can't replace any of the middle labels, for example, marketing.*.example.com. 
               
              * If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. 

              .. warning::

                 You can't use the * wildcard for resource records sets that have a type of NS. 

               
               

               

              You can use the * wildcard as the leftmost label in a domain name, for example, ``*.example.com`` . You can't use an * for one of the middle labels, for example, ``marketing.*.example.com`` . In addition, the * must replace the entire label; for example, you can't specify ``prod*.example.com`` .

              

            
            - **Type** *(string) --* **[REQUIRED]** 

              The DNS record type. For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``  

               

              Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.

               

              Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``  

               

              .. note::

                 

                SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <http://tools.ietf.org/html/rfc7208#section-14.1>`__ .

                 

               

              Values for alias resource record sets:

               

               
              * **CloudFront distributions:**  ``A``   If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` .  
               
              * **AWS Elastic Beanstalk environment that has a regionalized subdomain** : ``A``   
               
              * **ELB load balancers:**  ``A`` | ``AAAA``   
               
              * **Amazon S3 buckets:**  ``A``   
               
              * **Another resource record set in this hosted zone:** Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` . 
               

              

            
            - **SetIdentifier** *(string) --* 

               *Weighted, Latency, Geo, and Failover resource record sets only:* An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of ``SetIdentifier`` must be unique for each resource record set that has the same combination of DNS name and type. Omit ``SetIdentifier`` for any other types of record sets.

              

            
            - **Weight** *(integer) --* 

               *Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Amazon Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Amazon Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:

               

               
              * You must specify a value for the ``Weight`` element for every weighted resource record set. 
               
              * You can only specify one ``ResourceRecord`` per weighted resource record set. 
               
              * You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets. 
               
              * You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements. 
               
              * For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Amazon Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Amazon Route 53 Active-Active and Active-Passive Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`__ in the *Amazon Route 53 Developer Guide* . 
               

              

            
            - **Region** *(string) --* 

               *Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.

               

              .. note::

                 

                Creating latency and latency alias resource record sets in private hosted zones is not supported.

                 

               

              When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Amazon Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Amazon Route 53 then returns the value that is associated with the selected resource record set.

               

              Note the following:

               

               
              * You can only specify one ``ResourceRecord`` per latency resource record set. 
               
              * You can only create one latency resource record set for each Amazon EC2 Region. 
               
              * You aren't required to create latency resource record sets for all Amazon EC2 Regions. Amazon Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for. 
               
              * You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets. 
               

              

            
            - **GeoLocation** *(dict) --* 

               *Geo location resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` .

               

              .. note::

                 

                Creating geolocation and geolocation alias resource record sets in private hosted zones is not supported.

                 

               

              If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.

               

              You can't create two geolocation resource record sets that specify the same geographic location.

               

              The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements.

               

              .. warning::

                 

                Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Amazon Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` , which handles both queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Amazon Route 53 returns a "no answer" response for queries from those locations.

                 

               

              You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.

              

            
              - **ContinentCode** *(string) --* 

                The two-letter code for the continent.

                 

                Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``  

                 

                Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.

                

              
              - **CountryCode** *(string) --* 

                The two-letter code for the country.

                

              
              - **SubdivisionCode** *(string) --* 

                The code for the subdivision, for example, a state in the United States or a province in Canada.

                

              
            
            - **Failover** *(string) --* 

               *Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets. For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set.

               

              Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets:

               

               
              * When the primary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. 
               
              * When the primary resource record set is unhealthy and the secondary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the secondary resource record set. 
               
              * When the secondary resource record set is unhealthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. 
               
              * If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Amazon Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. 
               

               

              You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets.

               

              For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true.

               

              For more information about configuring failover for Amazon Route 53, see the following topics in the *Amazon Route 53 Developer Guide* : 

               

               
              * `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
               
              * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
               

              

            
            - **MultiValueAnswer** *(boolean) --* 

               *Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` . Note the following:

               

               
              * If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. 
               
              * If you don't associate a health check with a multivalue answer record, Amazon Route 53 always considers the record to be healthy. 
               
              * Amazon Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Amazon Route 53 responds to all DNS queries with all the healthy records. 
               
              * If you have more than eight healthy records, Amazon Route 53 responds to different DNS resolvers with different combinations of healthy records. 
               
              * When all records are unhealthy, Amazon Route 53 responds to DNS queries with up to eight unhealthy records. 
               
              * If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. 
               

               

              You can't create multivalue answer alias records.

              

            
            - **TTL** *(integer) --* 

              The resource record cache time to live (TTL), in seconds. Note the following:

               

               
              * If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target.  
               
              * If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status. 
               
              * All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` . 
               
              * If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` . 
               

              

            
            - **ResourceRecords** *(list) --* 

              Information about the resource records to act upon.

               

              .. note::

                 

                If you're creating an alias resource record set, omit ``ResourceRecords`` .

                 

              

            
              - *(dict) --* 

                Information specific to the resource record.

                 

                .. note::

                   

                  If you're creating an alias resource record set, omit ``ResourceRecord`` .

                   

                

              
                - **Value** *(string) --* **[REQUIRED]** 

                  The current or new DNS record value, not to exceed 4,000 characters. In the case of a ``DELETE`` action, if the current value does not match the actual value, an error is returned. For descriptions about how to format ``Value`` for different record types, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .

                   

                  You can specify more than one value for all record types except ``CNAME`` and ``SOA`` . 

                   

                  .. note::

                     

                    If you're creating an alias resource record set, omit ``Value`` .

                     

                  

                
              
          
            - **AliasTarget** *(dict) --* 

               *Alias resource record sets only:* Information about the CloudFront distribution, AWS Elastic Beanstalk environment, ELB load balancer, Amazon S3 bucket, or Amazon Route 53 resource record set to which you're redirecting queries. The AWS Elastic Beanstalk environment must have a regionalized subdomain.

               

              If you're creating resource records sets for a private hosted zone, note the following:

               

               
              * You can't create alias resource record sets for CloudFront distributions in a private hosted zone. 
               
              * Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported. 
               
              * For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__ in the *Amazon Route 53 Developer Guide* . 
               

              

            
              - **HostedZoneId** *(string) --* **[REQUIRED]** 

                 *Alias resource records sets only* : The value used depends on where you want to route traffic:

                  CloudFront distribution  

                Specify ``Z2FDTNDATAQYW2`` .

                 

                .. note::

                   

                  Alias resource record sets for CloudFront can't be created in a private zone.

                   

                  Elastic Beanstalk environment  

                Specify the hosted zone ID for the region in which you created the environment. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk <http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region>`__ in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* .

                  ELB load balancer  

                Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:

                 

                 
                * `Elastic Load Balancing <http://docs.aws.amazon.com/general/latest/gr/rande.html#elb_region>`__ table in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers. 
                 
                * **AWS Management Console** : Go to the Amazon EC2 page, choose **Load Balancers** in the navigation pane, select the load balancer, and get the value of the **Hosted zone** field on the **Description** tab. 
                 
                * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                   
                  * Application and Network Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                   

                 
                 
                * **AWS CLI** : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                   
                  * Application and Network Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                   

                 
                 

                  An Amazon S3 bucket configured as a static website  

                Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the `Amazon Simple Storage Service Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ table in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* .

                  Another Amazon Route 53 resource record set in your hosted zone  

                Specify the hosted zone ID of your hosted zone. (An alias resource record set can't reference a resource record set in a different hosted zone.)

                  

              
              - **DNSName** *(string) --* **[REQUIRED]** 

                 *Alias resource record sets only:* The value that you specify depends on where you want to route queries:

                  CloudFront distribution  

                Specify the domain name that CloudFront assigned when you created your distribution.

                 

                Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`__ in the *Amazon CloudFront Developer Guide* .

                  Elastic Beanstalk environment  

                Specify the ``CNAME`` attribute for the environment. (The environment must have a regionalized domain name.) You can use the following methods to get the value of the CNAME attribute:

                 

                 
                * *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 
                 
                * *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`__ in the *AWS Elastic Beanstalk API Reference* . 
                 
                * *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <http://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`__ in the *AWS Command Line Interface Reference* . 
                 

                  ELB load balancer  

                Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. 

                 

                 
                * **AWS Management Console** : Go to the EC2 page, choose **Load Balancers** in the navigation pane, choose the load balancer, choose the **Description** tab, and get the value of the **DNS name** field. (If you're routing traffic to a Classic Load Balancer, get the value that begins with **dualstack** .)  
                 
                * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__   
                   
                  * Application and Network Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__   
                   

                 
                 
                * **AWS CLI** : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__   
                   
                  * Application and Network Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__   
                   

                 
                 

                  Amazon S3 bucket that is configured as a static website  

                Specify the domain name of the Amazon S3 website endpoint in which you created the bucket, for example, ``s3-website-us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon Simple Storage Service (S3) Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`__ in the *Amazon Route 53 Developer Guide.*  

                  Another Amazon Route 53 resource record set  

                Specify the value of the ``Name`` element for a resource record set in the current hosted zone.

                  

              
              - **EvaluateTargetHealth** *(boolean) --* **[REQUIRED]** 

                 *Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets:* When ``EvaluateTargetHealth`` is ``true`` , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer, or the referenced resource record set.

                 

                Note the following:

                 

                 
                * You can't set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution. 
                 
                * If the AWS resource that you specify in ``AliasTarget`` is a resource record set or a group of resource record sets (for example, a group of weighted resource record sets), but it is not another alias resource record set, we recommend that you associate a health check with all of the resource record sets in the alias target. For more information, see `What Happens When You Omit Health Checks? <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`__ in the *Amazon Route 53 Developer Guide* . 
                 
                * If you specify an Elastic Beanstalk environment in ``HostedZoneId`` and ``DNSName`` , and if the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Amazon Route 53 routes queries to other available resources that are healthy, if any. If the environment contains a single EC2 instance, there are no special requirements. 
                 
                * If you specify an ELB load balancer in ``  AliasTarget `` , ELB routes queries only to the healthy EC2 instances that are registered with the load balancer. If no EC2 instances are healthy or if the load balancer itself is unhealthy, and if ``EvaluateTargetHealth`` is true for the corresponding alias resource record set, Amazon Route 53 routes queries to other resources. When you create a load balancer, you configure settings for ELB health checks; they're not Amazon Route 53 health checks, but they perform a similar function. Do not create Amazon Route 53 health checks for the EC2 instances that you register with an ELB load balancer. For more information, see `How Health Checks Work in More Complex Amazon Route 53 Configurations <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html>`__ in the *Amazon Route 53 Developer Guide* . 
                 
                * We recommend that you set ``EvaluateTargetHealth`` to true only when you have enough idle capacity to handle the failure of one or more endpoints. 
                 

                 

                For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__ in the *Amazon Route 53 Developer Guide* .

                

              
            
            - **HealthCheckId** *(string) --* 

              If you want Amazon Route 53 to return this resource record set in response to a DNS query only when a health check is passing, include the ``HealthCheckId`` element and specify the ID of the applicable health check.

               

              Amazon Route 53 determines whether a resource record set is healthy based on one of the following:

               

               
              * By periodically sending a request to the endpoint that is specified in the health check 
               
              * By aggregating the status of a specified group of health checks (calculated health checks) 
               
              * By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) 
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ .

               

              The ``HealthCheckId`` element is only useful when Amazon Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Amazon Route 53 to base the choice in part on the status of a health check. Configuring health checks only makes sense in the following configurations:

               

               
              * You're checking the health of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets, and you specify health check IDs for all of the resource record sets. If the health check for one resource record set specifies an endpoint that is not healthy, Amazon Route 53 stops responding to queries using the value for that resource record set. 
               
              * You set ``EvaluateTargetHealth`` to true for the resource record sets in a group of alias, weighted alias, latency alias, geolocation alias, or failover alias resource record sets, and you specify health check IDs for all of the resource record sets that are referenced by the alias resource record sets. 
               

               

              .. warning::

                 

                Amazon Route 53 doesn't check the health of the endpoint specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Amazon Route 53 checks the health of the endpoint that you specified in the health check. 

                 

               

              For geolocation resource record sets, if an endpoint is unhealthy, Amazon Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the United States, for North America, and for all locations. If the endpoint for the state resource record set is unhealthy, Amazon Route 53 checks the resource record sets for the United States, for North America, and for all locations (a resource record set for which the value of ``CountryCode`` is ``*`` ), in that order, until it finds a resource record set for which the endpoint is healthy. 

               

              If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets (example.com).

               

              .. warning::

                 

                n this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and then associate the health check with those resource record sets, health check results will be unpredictable.

                 

               

              For more information, see the following topics in the *Amazon Route 53 Developer Guide* :

               

               
              * `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
               
              * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
               

              

            
            - **TrafficPolicyInstanceId** *(string) --* 

              When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. ``TrafficPolicyInstanceId`` is the ID of the traffic policy instance that Amazon Route 53 created this resource record set for.

               

              .. warning::

                 

                To delete the resource record set that is associated with a traffic policy instance, use ``DeleteTrafficPolicyInstance`` . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ``ChangeResourceRecordSets`` , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use. 

                 

              

            
          
        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type containing the response for the request.

        
        

        - **ChangeInfo** *(dict) --* 

          A complex type that contains information about changes made to your hosted zone.

           

          This element contains an ID that you use when performing a  GetChange action to get detailed information about the change.

          
          

          - **Id** *(string) --* 

            The ID of the request.

            
          

          - **Status** *(string) --* 

            The current state of the request. ``PENDING`` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

            
          

          - **SubmittedAt** *(datetime) --* 

            The date and time that the change request was submitted in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

            
          

          - **Comment** *(string) --* 

            A complex type that describes change information about changes made to your hosted zone.

             

            This element contains an ID that you use when performing a  GetChange action to get detailed information about the change.

            
      
    

  .. py:method:: change_tags_for_resource(**kwargs)

    

    Adds, edits, or deletes tags for a health check or a hosted zone.

     

    For information about using tags for cost allocation, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the *AWS Billing and Cost Management User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ChangeTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.change_tags_for_resource(
          ResourceType='healthcheck'|'hostedzone',
          ResourceId='string',
          AddTags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          RemoveTagKeys=[
              'string',
          ]
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the resource.

       

       
      * The resource type for health checks is ``healthcheck`` . 
       
      * The resource type for hosted zones is ``hostedzone`` . 
       

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The ID of the resource for which you want to add, change, or delete tags.

      

    
    :type AddTags: list
    :param AddTags: 

      A complex type that contains a list of the tags that you want to add to the specified health check or hosted zone and/or the tags that you want to edit ``Value`` for.

       

      You can add a maximum of 10 tags to a health check or a hosted zone.

      

    
      - *(dict) --* 

        A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

        

      
        - **Key** *(string) --* 

          The value of ``Key`` depends on the operation that you want to perform:

           

           
          * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to give the new tag. 
           
          * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value`` for. 
           
          * **Delete a key** : ``Key`` is the name of the tag you want to remove. 
           
          * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon Route 53 console, the list of your health checks includes a **Name** column that lets you see the name that you've given to each health check. 
           

          

        
        - **Value** *(string) --* 

          The value of ``Value`` depends on the operation that you want to perform:

           

           
          * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you want to give the new tag. 
           
          * **Edit a tag** : ``Value`` is the new value that you want to assign the tag. 
           

          

        
      
  
    :type RemoveTagKeys: list
    :param RemoveTagKeys: 

      A complex type that contains a list of the tags that you want to delete from the specified health check or hosted zone. You can specify up to 10 keys.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Empty response for the request.

        
    

  .. py:method:: create_health_check(**kwargs)

    

    Creates a new health check.

     

    For information about adding health checks to resource record sets, see  ResourceRecordSet$HealthCheckId in  ChangeResourceRecordSets . 

     

     **ELB Load Balancers**  

     

    If you're registering EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the EC2 instances. When you register an EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to an Amazon Route 53 health check.

     

     **Private Hosted Zones**  

     

    You can associate health checks with failover resource record sets in a private hosted zone. Note the following:

     

     
    * Amazon Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC. 
     
    * You can configure a health checker to check the health of an external resource that the instance relies on, such as a database server. 
     
    * You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the state of the alarm. For example, you might create a CloudWatch metric that checks the status of the Amazon EC2 ``StatusCheckFailed`` metric, add an alarm to the metric, and then create a health check that is based on the state of the alarm. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the `Amazon CloudWatch User Guide <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html>`__ . 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateHealthCheck>`_    


    **Request Syntax** 
    ::

      response = client.create_health_check(
          CallerReference='string',
          HealthCheckConfig={
              'IPAddress': 'string',
              'Port': 123,
              'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
              'ResourcePath': 'string',
              'FullyQualifiedDomainName': 'string',
              'SearchString': 'string',
              'RequestInterval': 123,
              'FailureThreshold': 123,
              'MeasureLatency': True|False,
              'Inverted': True|False,
              'HealthThreshold': 123,
              'ChildHealthChecks': [
                  'string',
              ],
              'EnableSNI': True|False,
              'Regions': [
                  'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
              ],
              'AlarmIdentifier': {
                  'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                  'Name': 'string'
              },
              'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
          }
      )
    :type CallerReference: string
    :param CallerReference: **[REQUIRED]** 

      A unique string that identifies the request and that allows you to retry a failed ``CreateHealthCheck`` request without the risk of creating two identical health checks:

       

       
      * If you send a ``CreateHealthCheck`` request with the same ``CallerReference`` and settings as a previous request, and if the health check doesn't exist, Amazon Route 53 creates the health check. If the health check does exist, Amazon Route 53 returns the settings for the existing health check. 
       
      * If you send a ``CreateHealthCheck`` request with the same ``CallerReference`` as a deleted health check, regardless of the settings, Amazon Route 53 returns a ``HealthCheckAlreadyExists`` error. 
       
      * If you send a ``CreateHealthCheck`` request with the same ``CallerReference`` as an existing health check but with different settings, Amazon Route 53 returns a ``HealthCheckAlreadyExists`` error. 
       
      * If you send a ``CreateHealthCheck`` request with a unique ``CallerReference`` but settings identical to an existing health check, Amazon Route 53 creates the health check. 
       

      

    
    :type HealthCheckConfig: dict
    :param HealthCheckConfig: **[REQUIRED]** 

      A complex type that contains the response to a ``CreateHealthCheck`` request. 

      

    
      - **IPAddress** *(string) --* 

        The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Amazon Route 53 then checks the health of the endpoint.

         

        Use one of the following formats for the value of ``IPAddress`` : 

         

         
        * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
         
        * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
         

         

        If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.

         

        For more information, see  HealthCheckConfig$FullyQualifiedDomainName .

         

        Constraints: Amazon Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

         

         
        * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
         
        * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
         
        * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
         

         

        When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

        

      
      - **Port** *(integer) --* 

        The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

        

      
      - **Type** *(string) --* **[REQUIRED]** 

        The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

         

        .. warning::

           

          You can't change the value of ``Type`` after you create a health check.

           

         

        You can create the following types of health checks:

         

         
        * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
         
        * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

        .. warning::

           If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

         
         
        * **HTTP_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
         
        * **HTTPS_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
         
        * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
         
        * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .  
         
        * **CALCULATED** : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .  
         

         

        For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

        

      
      - **ResourcePath** *(string) --* 

        The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. 

        

      
      - **FullyQualifiedDomainName** *(string) --* 

        Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

         

         **If you specify a value for**  ``IPAddress`` :

         

        Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks.

         

        When Amazon Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

         

         
        * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.  
         
        * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
         
        * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Amazon Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. 
         

         

        If you don't specify a value for ``FullyQualifiedDomainName`` , Amazon Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

         

         **If you don't specify a value for ``IPAddress`` ** :

         

        Amazon Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Amazon Route 53 then checks the health of the endpoint.

         

        .. note::

           

          If you don't specify a value for ``IPAddress`` , Amazon Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

           

         

        If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

         

        .. warning::

           

          In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

           

         

        In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Amazon Route 53 doesn't pass a ``Host`` header.

        

      
      - **SearchString** *(string) --* 

        If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.

         

        Amazon Route 53 considers case when searching for ``SearchString`` in the response body. 

        

      
      - **RequestInterval** *(integer) --* 

        The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Amazon Route 53 health checker makes requests at this interval.

         

        .. warning::

           

          You can't change the value of ``RequestInterval`` after you create a health check.

           

         

        If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

        

      
      - **FailureThreshold** *(integer) --* 

        The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

         

        If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

        

      
      - **MeasureLatency** *(boolean) --* 

        Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Amazon Route 53 console.

         

        .. warning::

           

          You can't change the value of ``MeasureLatency`` after you create a health check.

           

        

      
      - **Inverted** *(boolean) --* 

        Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

        

      
      - **HealthThreshold** *(integer) --* 

        The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.

         

        Note the following:

         

         
        * If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy. 
         
        * If you specify ``0`` , Amazon Route 53 always considers this health check to be healthy. 
         

        

      
      - **ChildHealthChecks** *(list) --* 

        (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

        

      
        - *(string) --* 

        
    
      - **EnableSNI** *(boolean) --* 

        Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

         

        Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

         

        The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

        

      
      - **Regions** *(list) --* 

        A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

         

        If you don't specify any regions, Amazon Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .

         

        If you update a health check to remove a region that has been performing health checks, Amazon Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions). 

        

      
        - *(string) --* 

        
    
      - **AlarmIdentifier** *(dict) --* 

        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

        

      
        - **Region** *(string) --* **[REQUIRED]** 

          A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

           

          For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

          

        
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

          

        
      
      - **InsufficientDataHealthStatus** *(string) --* 

        When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

         

         
        * ``Healthy`` : Amazon Route 53 considers the health check to be healthy. 
         
        * ``Unhealthy`` : Amazon Route 53 considers the health check to be unhealthy. 
         
        * ``LastKnownStatus`` : Amazon Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
         

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthCheck': {
                'Id': 'string',
                'CallerReference': 'string',
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                },
                'HealthCheckConfig': {
                    'IPAddress': 'string',
                    'Port': 123,
                    'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                    'ResourcePath': 'string',
                    'FullyQualifiedDomainName': 'string',
                    'SearchString': 'string',
                    'RequestInterval': 123,
                    'FailureThreshold': 123,
                    'MeasureLatency': True|False,
                    'Inverted': True|False,
                    'HealthThreshold': 123,
                    'ChildHealthChecks': [
                        'string',
                    ],
                    'EnableSNI': True|False,
                    'Regions': [
                        'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                    ],
                    'AlarmIdentifier': {
                        'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                        'Name': 'string'
                    },
                    'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
                },
                'HealthCheckVersion': 123,
                'CloudWatchAlarmConfiguration': {
                    'EvaluationPeriods': 123,
                    'Threshold': 123.0,
                    'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                    'Period': 123,
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            },
            'Location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type containing the response information for the new health check.

        
        

        - **HealthCheck** *(dict) --* 

          A complex type that contains identifying information about the health check.

          
          

          - **Id** *(string) --* 

            The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. 

            
          

          - **CallerReference** *(string) --* 

            A unique string that you specified when you created the health check.

            
          

          - **LinkedService** *(dict) --* 

            If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can't edit or delete it using Amazon Route 53. 

            
            

            - **ServicePrincipal** *(string) --* 

              If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
            

            - **Description** *(string) --* 

              If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
        
          

          - **HealthCheckConfig** *(dict) --* 

            A complex type that contains detailed information about one health check.

            
            

            - **IPAddress** *(string) --* 

              The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Amazon Route 53 then checks the health of the endpoint.

               

              Use one of the following formats for the value of ``IPAddress`` : 

               

               
              * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
               
              * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
               

               

              If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.

               

              For more information, see  HealthCheckConfig$FullyQualifiedDomainName .

               

              Constraints: Amazon Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

               

               
              * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
               
              * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
               
              * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
               

               

              When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

              
            

            - **Port** *(integer) --* 

              The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

              
            

            - **Type** *(string) --* 

              The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

               

              .. warning::

                 

                You can't change the value of ``Type`` after you create a health check.

                 

               

              You can create the following types of health checks:

               

               
              * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
               
              * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

              .. warning::

                 If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

               
               
              * **HTTP_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
               
              * **HTTPS_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
               
              * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
               
              * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .  
               
              * **CALCULATED** : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .  
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

              
            

            - **ResourcePath** *(string) --* 

              The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. 

              
            

            - **FullyQualifiedDomainName** *(string) --* 

              Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

               

               **If you specify a value for**  ``IPAddress`` :

               

              Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks.

               

              When Amazon Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

               

               
              * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.  
               
              * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
               
              * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Amazon Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. 
               

               

              If you don't specify a value for ``FullyQualifiedDomainName`` , Amazon Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

               

               **If you don't specify a value for ``IPAddress`` ** :

               

              Amazon Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Amazon Route 53 then checks the health of the endpoint.

               

              .. note::

                 

                If you don't specify a value for ``IPAddress`` , Amazon Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

                 

               

              If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

               

              .. warning::

                 

                In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

                 

               

              In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Amazon Route 53 doesn't pass a ``Host`` header.

              
            

            - **SearchString** *(string) --* 

              If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.

               

              Amazon Route 53 considers case when searching for ``SearchString`` in the response body. 

              
            

            - **RequestInterval** *(integer) --* 

              The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Amazon Route 53 health checker makes requests at this interval.

               

              .. warning::

                 

                You can't change the value of ``RequestInterval`` after you create a health check.

                 

               

              If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

              
            

            - **FailureThreshold** *(integer) --* 

              The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

              
            

            - **MeasureLatency** *(boolean) --* 

              Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Amazon Route 53 console.

               

              .. warning::

                 

                You can't change the value of ``MeasureLatency`` after you create a health check.

                 

              
            

            - **Inverted** *(boolean) --* 

              Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

              
            

            - **HealthThreshold** *(integer) --* 

              The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.

               

              Note the following:

               

               
              * If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy. 
               
              * If you specify ``0`` , Amazon Route 53 always considers this health check to be healthy. 
               

              
            

            - **ChildHealthChecks** *(list) --* 

              (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

              
              

              - *(string) --* 
          
            

            - **EnableSNI** *(boolean) --* 

              Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

               

              Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

               

              The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

              
            

            - **Regions** *(list) --* 

              A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

               

              If you don't specify any regions, Amazon Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .

               

              If you update a health check to remove a region that has been performing health checks, Amazon Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions). 

              
              

              - *(string) --* 
          
            

            - **AlarmIdentifier** *(dict) --* 

              A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

              
              

              - **Region** *(string) --* 

                A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                 

                For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

                
              

              - **Name** *(string) --* 

                The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                
          
            

            - **InsufficientDataHealthStatus** *(string) --* 

              When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

               

               
              * ``Healthy`` : Amazon Route 53 considers the health check to be healthy. 
               
              * ``Unhealthy`` : Amazon Route 53 considers the health check to be unhealthy. 
               
              * ``LastKnownStatus`` : Amazon Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
               

              
        
          

          - **HealthCheckVersion** *(integer) --* 

            The version of the health check. You can optionally pass this value in a call to ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

            
          

          - **CloudWatchAlarmConfiguration** *(dict) --* 

            A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

            
            

            - **EvaluationPeriods** *(integer) --* 

              For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

              
            

            - **Threshold** *(float) --* 

              For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

              
            

            - **ComparisonOperator** *(string) --* 

              For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

              
            

            - **Period** *(integer) --* 

              For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

              
            

            - **MetricName** *(string) --* 

              The name of the CloudWatch metric that the alarm is associated with.

              
            

            - **Namespace** *(string) --* 

              The namespace of the metric that the alarm is associated with. For more information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

              
            

            - **Statistic** *(string) --* 

              For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

              
            

            - **Dimensions** *(list) --* 

              For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

              
              

              - *(dict) --* 

                For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

                
                

                - **Name** *(string) --* 

                  For the metric that the CloudWatch alarm is associated with, the name of one dimension.

                  
                

                - **Value** *(string) --* 

                  For the metric that the CloudWatch alarm is associated with, the value of one dimension.

                  
            
          
        
      
        

        - **Location** *(string) --* 

          The unique URL representing the new health check.

          
    

  .. py:method:: create_hosted_zone(**kwargs)

    

    Creates a new public hosted zone, which you use to specify how the Domain Name System (DNS) routes traffic on the Internet for a domain, such as example.com, and its subdomains. 

     

    .. warning::

       

      You can't convert a public hosted zones to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.

       

     

    For more information about charges for hosted zones, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

     

    Note the following:

     

     
    * You can't create a hosted zone for a top-level domain (TLD). 
     
    * Amazon Route 53 automatically creates a default SOA record and four NS records for the zone. For more information about SOA and NS records, see `NS and SOA Records that Amazon Route 53 Creates for a Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/SOA-NSrecords.html>`__ in the *Amazon Route 53 Developer Guide* . If you want to use the same name servers for multiple hosted zones, you can optionally associate a reusable delegation set with the hosted zone. See the ``DelegationSetId`` element. 
     
    * If your domain is registered with a registrar other than Amazon Route 53, you must update the name servers with your registrar to make Amazon Route 53 your DNS service. For more information, see `Configuring Amazon Route 53 as your DNS Service <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creating-migrating.html>`__ in the *Amazon Route 53 Developer Guide* .  
     

     

    When you submit a ``CreateHostedZone`` request, the initial status of the hosted zone is ``PENDING`` . This means that the NS and SOA records are not yet available on all Amazon Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to ``INSYNC`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateHostedZone>`_    


    **Request Syntax** 
    ::

      response = client.create_hosted_zone(
          Name='string',
          VPC={
              'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
              'VPCId': 'string'
          },
          CallerReference='string',
          HostedZoneConfig={
              'Comment': 'string',
              'PrivateZone': True|False
          },
          DelegationSetId='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name, for example, *www.example.com* . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Amazon Route 53 treats *www.example.com* (without a trailing dot) and *www.example.com.* (with a trailing dot) as identical.

       

      If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Amazon Route 53, change the name servers for your domain to the set of ``NameServers`` that ``CreateHostedZone`` returns in ``DelegationSet`` .

      

    
    :type VPC: dict
    :param VPC: 

      (Private hosted zones only) A complex type that contains information about the Amazon VPC that you're associating with this hosted zone.

       

      You can specify only one Amazon VPC when you create a private hosted zone. To associate additional Amazon VPCs with the hosted zone, use  AssociateVPCWithHostedZone after you create a hosted zone.

      

    
      - **VPCRegion** *(string) --* 

        (Private hosted zones only) The region in which you created an Amazon VPC.

        

      
      - **VPCId** *(string) --* 

        (Private hosted zones only) The ID of an Amazon VPC. 

        

      
    
    :type CallerReference: string
    :param CallerReference: **[REQUIRED]** 

      A unique string that identifies the request and that allows failed ``CreateHostedZone`` requests to be retried without the risk of executing the operation twice. You must use a unique ``CallerReference`` string every time you submit a ``CreateHostedZone`` request. ``CallerReference`` can be any unique string, for example, a date/time stamp.

      

    
    :type HostedZoneConfig: dict
    :param HostedZoneConfig: 

      (Optional) A complex type that contains the following optional values:

       

       
      * For public and private hosted zones, an optional comment 
       
      * For private hosted zones, an optional ``PrivateZone`` element 
       

       

      If you don't specify a comment or the ``PrivateZone`` element, omit ``HostedZoneConfig`` and the other elements.

      

    
      - **Comment** *(string) --* 

        Any comments that you want to include about the hosted zone.

        

      
      - **PrivateZone** *(boolean) --* 

        A value that indicates whether this is a private hosted zone.

        

      
    
    :type DelegationSetId: string
    :param DelegationSetId: 

      If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see  CreateReusableDelegationSet .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZone': {
                'Id': 'string',
                'Name': 'string',
                'CallerReference': 'string',
                'Config': {
                    'Comment': 'string',
                    'PrivateZone': True|False
                },
                'ResourceRecordSetCount': 123,
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                }
            },
            'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
            },
            'DelegationSet': {
                'Id': 'string',
                'CallerReference': 'string',
                'NameServers': [
                    'string',
                ]
            },
            'VPC': {
                'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
                'VPCId': 'string'
            },
            'Location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type containing the response information for the hosted zone.

        
        

        - **HostedZone** *(dict) --* 

          A complex type that contains general information about the hosted zone.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the hosted zone when you created it.

            
          

          - **Name** *(string) --* 

            The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

             

            For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see  CreateHostedZone .

            
          

          - **CallerReference** *(string) --* 

            The value that you specified for ``CallerReference`` when you created the hosted zone.

            
          

          - **Config** *(dict) --* 

            A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and ``Comment`` elements don't appear in the response.

            
            

            - **Comment** *(string) --* 

              Any comments that you want to include about the hosted zone.

              
            

            - **PrivateZone** *(boolean) --* 

              A value that indicates whether this is a private hosted zone.

              
        
          

          - **ResourceRecordSetCount** *(integer) --* 

            The number of resource record sets in the hosted zone.

            
          

          - **LinkedService** *(dict) --* 

            If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Amazon Route 53. 

            
            

            - **ServicePrincipal** *(string) --* 

              If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
            

            - **Description** *(string) --* 

              If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
        
      
        

        - **ChangeInfo** *(dict) --* 

          A complex type that contains information about the ``CreateHostedZone`` request.

          
          

          - **Id** *(string) --* 

            The ID of the request.

            
          

          - **Status** *(string) --* 

            The current state of the request. ``PENDING`` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

            
          

          - **SubmittedAt** *(datetime) --* 

            The date and time that the change request was submitted in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

            
          

          - **Comment** *(string) --* 

            A complex type that describes change information about changes made to your hosted zone.

             

            This element contains an ID that you use when performing a  GetChange action to get detailed information about the change.

            
      
        

        - **DelegationSet** *(dict) --* 

          A complex type that describes the name servers for this hosted zone.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigns to a reusable delegation set.

            
          

          - **CallerReference** *(string) --* 

            The value that you specified for ``CallerReference`` when you created the reusable delegation set.

            
          

          - **NameServers** *(list) --* 

            A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

            
            

            - *(string) --* 
        
      
        

        - **VPC** *(dict) --* 

          A complex type that contains information about an Amazon VPC that you associated with this hosted zone.

          
          

          - **VPCRegion** *(string) --* 

            (Private hosted zones only) The region in which you created an Amazon VPC.

            
          

          - **VPCId** *(string) --* 

            (Private hosted zones only) The ID of an Amazon VPC. 

            
      
        

        - **Location** *(string) --* 

          The unique URL representing the new hosted zone.

          
    

  .. py:method:: create_query_logging_config(**kwargs)

    

    Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.

     

    DNS query logs contain information about the queries that Amazon Route 53 receives for a specified public hosted zone, such as the following:

     

     
    * Amazon Route 53 edge location that responded to the DNS query 
     
    * Domain or subdomain that was requested 
     
    * DNS record type, such as A or AAAA 
     
    * DNS response code, such as ``NoError`` or ``ServFail``   
     

      Log Group and Resource Policy  

    Before you create a query logging configuration, perform the following operations.

     

    .. note::

       

      If you create a query logging configuration using the Amazon Route 53 console, Amazon Route 53 performs these operations automatically.

       

     

     
    * Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following: 

       
      * You must create the log group in the us-east-1 region. 
       
      * You must use the same AWS account to create the log group and the hosted zone that you want to configure query logging for. 
       
      * When you create log groups for query logging, we recommend that you use a consistent prefix, for example:  ``/aws/route53/*hosted zone name* ``   In the next step, you'll create a resource policy, which controls access to one or more log groups and the associated AWS resources, such as Amazon Route 53 hosted zones. There's a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging. 
       

     
     
    * Create a CloudWatch Logs resource policy, and give it the permissions that Amazon Route 53 needs to create log streams and to send query logs to log streams. For the value of ``Resource`` , specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with ``*`` , for example:  ``arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*``   

    .. note::

       You can't use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the AWS SDKs, or the AWS CLI. 

     
     

      Log Streams and Edge Locations  

    When Amazon Route 53 finishes creating the configuration for DNS query logging, it does the following:

     

     
    * Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Amazon Route 53 responds to for that edge location. 
     
    * Begins to send query logs to the applicable log stream. 
     

     

    The name of each log stream is in the following format:

     

     `` *hosted zone ID* /*edge location code* ``  

     

    The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Amazon Route 53 Global Network" on the `Amazon Route 53 Product Details <http://aws.amazon.com/route53/details/>`__ page.

      Queries That Are Logged  

    Query logs contain only the queries that DNS resolvers forward to Amazon Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn't forward another query to Amazon Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see `Routing Internet Traffic to Your Website or Web Application <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html>`__ in the *Amazon Route 53 Developer Guide* .

      Log File Format  

    For a list of the values in each query log and the format of each value, see `Logging DNS Queries <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html>`__ in the *Amazon Route 53 Developer Guide* .

      Pricing  

    For information about charges for query logs, see `Amazon CloudWatch Pricing <http://aws.amazon.com/cloudwatch/pricing/>`__ .

      How to Stop Logging  

    If you want Amazon Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see  DeleteQueryLoggingConfig .

      

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateQueryLoggingConfig>`_    


    **Request Syntax** 
    ::

      response = client.create_query_logging_config(
          HostedZoneId='string',
          CloudWatchLogsLogGroupArn='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone that you want to log queries for. You can log queries only for public hosted zones.

      

    
    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) for the log group that you want to Amazon Route 53 to send query logs to. This is the format of the ARN:

       

      arn:aws:logs:*region* :*account-id* :log-group:*log_group_name*  

       

      To get the ARN for a log group, you can use the CloudWatch console, the `DescribeLogGroups <http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html>`__ API action, the `describe-log-groups <http://docs.aws.amazon.com/cli/latest/reference/logs/describe-log-groups.html>`__ command, or the applicable command in one of the AWS SDKs.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'QueryLoggingConfig': {
                'Id': 'string',
                'HostedZoneId': 'string',
                'CloudWatchLogsLogGroupArn': 'string'
            },
            'Location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryLoggingConfig** *(dict) --* 

          A complex type that contains the ID for a query logging configuration, the ID of the hosted zone that you want to log queries for, and the ARN for the log group that you want Amazon Route 53 to send query logs to.

          
          

          - **Id** *(string) --* 

            The ID for a configuration for DNS query logging.

            
          

          - **HostedZoneId** *(string) --* 

            The ID of the hosted zone that CloudWatch Logs is logging queries for. 

            
          

          - **CloudWatchLogsLogGroupArn** *(string) --* 

            The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.

            
      
        

        - **Location** *(string) --* 

          The unique URL representing the new query logging configuration.

          
    

  .. py:method:: create_reusable_delegation_set(**kwargs)

    

    Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones. If a hosted zoned ID is specified, ``CreateReusableDelegationSet`` marks the delegation set associated with that zone as reusable

     

    .. note::

       

      A reusable delegation set can't be associated with a private hosted zone.

       

     

    For information on how to use a reusable delegation set to configure white label name servers, see `Configuring White Label Name Servers <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-name-servers.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateReusableDelegationSet>`_    


    **Request Syntax** 
    ::

      response = client.create_reusable_delegation_set(
          CallerReference='string',
          HostedZoneId='string'
      )
    :type CallerReference: string
    :param CallerReference: **[REQUIRED]** 

      A unique string that identifies the request, and that allows you to retry failed ``CreateReusableDelegationSet`` requests without the risk of executing the operation twice. You must use a unique ``CallerReference`` string every time you submit a ``CreateReusableDelegationSet`` request. ``CallerReference`` can be any unique string, for example a date/time stamp.

      

    
    :type HostedZoneId: string
    :param HostedZoneId: 

      If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DelegationSet': {
                'Id': 'string',
                'CallerReference': 'string',
                'NameServers': [
                    'string',
                ]
            },
            'Location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DelegationSet** *(dict) --* 

          A complex type that contains name server information.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigns to a reusable delegation set.

            
          

          - **CallerReference** *(string) --* 

            The value that you specified for ``CallerReference`` when you created the reusable delegation set.

            
          

          - **NameServers** *(list) --* 

            A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

            
            

            - *(string) --* 
        
      
        

        - **Location** *(string) --* 

          The unique URL representing the new reusable delegation set.

          
    

  .. py:method:: create_traffic_policy(**kwargs)

    

    Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateTrafficPolicy>`_    


    **Request Syntax** 
    ::

      response = client.create_traffic_policy(
          Name='string',
          Document='string',
          Comment='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the traffic policy.

      

    
    :type Document: string
    :param Document: **[REQUIRED]** 

      The definition of this traffic policy in JSON format. For more information, see `Traffic Policy Document Format <http://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__ .

      

    
    :type Comment: string
    :param Comment: 

      (Optional) Any comments that you want to include about the traffic policy.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicy': {
                'Id': 'string',
                'Version': 123,
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                'Document': 'string',
                'Comment': 'string'
            },
            'Location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the ``CreateTrafficPolicy`` request.

        
        

        - **TrafficPolicy** *(dict) --* 

          A complex type that contains settings for the new traffic policy.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to a traffic policy when you created it.

            
          

          - **Version** *(integer) --* 

            The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of ``Version`` is always 1.

            
          

          - **Name** *(string) --* 

            The name that you specified when you created the traffic policy.

            
          

          - **Type** *(string) --* 

            The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

            
          

          - **Document** *(string) --* 

            The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the JSON format, see `Traffic Policy Document Format <http://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__ .

            
          

          - **Comment** *(string) --* 

            The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

            
      
        

        - **Location** *(string) --* 

          A unique URL that represents a new traffic policy.

          
    

  .. py:method:: create_traffic_policy_instance(**kwargs)

    

    Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version. In addition, ``CreateTrafficPolicyInstance`` associates the resource record sets with a specified domain name (such as example.com) or subdomain name (such as www.example.com). Amazon Route 53 responds to DNS queries for the domain or subdomain name by using the resource record sets that ``CreateTrafficPolicyInstance`` created.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateTrafficPolicyInstance>`_    


    **Request Syntax** 
    ::

      response = client.create_traffic_policy_instance(
          HostedZoneId='string',
          Name='string',
          TTL=123,
          TrafficPolicyId='string',
          TrafficPolicyVersion=123
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone in which you want Amazon Route 53 to create resource record sets by using the configuration in a traffic policy.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Amazon Route 53 creates for this traffic policy instance.

      

    
    :type TTL: integer
    :param TTL: **[REQUIRED]** 

      (Optional) The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.

      

    
    :type TrafficPolicyId: string
    :param TrafficPolicyId: **[REQUIRED]** 

      The ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.

      

    
    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: **[REQUIRED]** 

      The version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicyInstance': {
                'Id': 'string',
                'HostedZoneId': 'string',
                'Name': 'string',
                'TTL': 123,
                'State': 'string',
                'Message': 'string',
                'TrafficPolicyId': 'string',
                'TrafficPolicyVersion': 123,
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
            },
            'Location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the ``CreateTrafficPolicyInstance`` request.

        
        

        - **TrafficPolicyInstance** *(dict) --* 

          A complex type that contains settings for the new traffic policy instance.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the new traffic policy instance.

            
          

          - **HostedZoneId** *(string) --* 

            The ID of the hosted zone that Amazon Route 53 created resource record sets in.

            
          

          - **Name** *(string) --* 

            The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance. 

            
          

          - **TTL** *(integer) --* 

            The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

            
          

          - **State** *(string) --* 

            The value of ``State`` is one of the following values:

              Applied  

            Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Amazon Route 53 edge locations.

              Creating  

            Amazon Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

              Failed  

            Amazon Route 53 wasn't able to create or update the resource record sets. When the value of ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to fail.

              
          

          - **Message** *(string) --* 

            If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is another value, ``Message`` is empty.

            
          

          - **TrafficPolicyId** *(string) --* 

            The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

            
          

          - **TrafficPolicyVersion** *(integer) --* 

            The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

            
          

          - **TrafficPolicyType** *(string) --* 

            The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance. 

            
      
        

        - **Location** *(string) --* 

          A unique URL that represents a new traffic policy instance.

          
    

  .. py:method:: create_traffic_policy_version(**kwargs)

    

    Creates a new version of an existing traffic policy. When you create a new version of a traffic policy, you specify the ID of the traffic policy that you want to update and a JSON-formatted document that describes the new version. You use traffic policies to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com). You can create a maximum of 1000 versions of a traffic policy. If you reach the limit and need to create another version, you'll need to start a new traffic policy.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateTrafficPolicyVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_traffic_policy_version(
          Id='string',
          Document='string',
          Comment='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the traffic policy for which you want to create a new version.

      

    
    :type Document: string
    :param Document: **[REQUIRED]** 

      The definition of this version of the traffic policy, in JSON format. You specified the JSON in the ``CreateTrafficPolicyVersion`` request. For more information about the JSON format, see  CreateTrafficPolicy .

      

    
    :type Comment: string
    :param Comment: 

      The comment that you specified in the ``CreateTrafficPolicyVersion`` request, if any.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicy': {
                'Id': 'string',
                'Version': 123,
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                'Document': 'string',
                'Comment': 'string'
            },
            'Location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the ``CreateTrafficPolicyVersion`` request.

        
        

        - **TrafficPolicy** *(dict) --* 

          A complex type that contains settings for the new version of the traffic policy.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to a traffic policy when you created it.

            
          

          - **Version** *(integer) --* 

            The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of ``Version`` is always 1.

            
          

          - **Name** *(string) --* 

            The name that you specified when you created the traffic policy.

            
          

          - **Type** *(string) --* 

            The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

            
          

          - **Document** *(string) --* 

            The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the JSON format, see `Traffic Policy Document Format <http://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__ .

            
          

          - **Comment** *(string) --* 

            The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

            
      
        

        - **Location** *(string) --* 

          A unique URL that represents a new traffic policy version.

          
    

  .. py:method:: create_vpc_association_authorization(**kwargs)

    

    Authorizes the AWS account that created a specified VPC to submit an ``AssociateVPCWithHostedZone`` request to associate the VPC with a specified hosted zone that was created by a different account. To submit a ``CreateVPCAssociationAuthorization`` request, you must use the account that created the hosted zone. After you authorize the association, use the account that created the VPC to submit an ``AssociateVPCWithHostedZone`` request.

     

    .. note::

       

      If you want to associate multiple VPCs that you created by using one account with a hosted zone that you created by using a different account, you must submit one authorization request for each VPC.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateVPCAssociationAuthorization>`_    


    **Request Syntax** 
    ::

      response = client.create_vpc_association_authorization(
          HostedZoneId='string',
          VPC={
              'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
              'VPCId': 'string'
          }
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the private hosted zone that you want to authorize associating a VPC with.

      

    
    :type VPC: dict
    :param VPC: **[REQUIRED]** 

      A complex type that contains the VPC ID and region for the VPC that you want to authorize associating with your hosted zone.

      

    
      - **VPCRegion** *(string) --* 

        (Private hosted zones only) The region in which you created an Amazon VPC.

        

      
      - **VPCId** *(string) --* 

        (Private hosted zones only) The ID of an Amazon VPC. 

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZoneId': 'string',
            'VPC': {
                'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
                'VPCId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information from a ``CreateVPCAssociationAuthorization`` request.

        
        

        - **HostedZoneId** *(string) --* 

          The ID of the hosted zone that you authorized associating a VPC with.

          
        

        - **VPC** *(dict) --* 

          The VPC that you authorized associating with a hosted zone.

          
          

          - **VPCRegion** *(string) --* 

            (Private hosted zones only) The region in which you created an Amazon VPC.

            
          

          - **VPCId** *(string) --* 

            (Private hosted zones only) The ID of an Amazon VPC. 

            
      
    

  .. py:method:: delete_health_check(**kwargs)

    

    Deletes a health check.

     

    .. warning::

       

      Amazon Route 53 does not prevent you from deleting a health check even if the health check is associated with one or more resource record sets. If you delete a health check and you don't update the associated resource record sets, the future status of the health check can't be predicted and may change. This will affect the routing of DNS queries for your DNS failover configuration. For more information, see `Replacing and Deleting Health Checks <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html#health-checks-deleting.html>`__ in the *Amazon Route 53 Developer Guide* .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DeleteHealthCheck>`_    


    **Request Syntax** 
    ::

      response = client.delete_health_check(
          HealthCheckId='string'
      )
    :type HealthCheckId: string
    :param HealthCheckId: **[REQUIRED]** 

      The ID of the health check that you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element.

        
    

  .. py:method:: delete_hosted_zone(**kwargs)

    

    Deletes a hosted zone.

     

    .. warning::

       

      If the name servers for the hosted zone are associated with a domain and if you want to make the domain unavailable on the Internet, we recommend that you delete the name servers from the domain to prevent future DNS queries from possibly being misrouted. If the domain is registered with Amazon Route 53, see ``UpdateDomainNameservers`` . If the domain is registered with another registrar, use the method provided by the registrar to delete name servers for the domain.

       

      Some domain registries don't allow you to remove all of the name servers for a domain. If the registry for your domain requires one or more name servers, we recommend that you delete the hosted zone only if you transfer DNS service to another service provider, and you replace the name servers for the domain with name servers from the new provider.

       

     

    You can delete a hosted zone only if it contains only the default SOA record and NS resource record sets. If the hosted zone contains other resource record sets, you must delete them before you can delete the hosted zone. If you try to delete a hosted zone that contains other resource record sets, the request fails, and Amazon Route 53 returns a ``HostedZoneNotEmpty`` error. For information about deleting records from your hosted zone, see  ChangeResourceRecordSets .

     

    To verify that the hosted zone has been deleted, do one of the following:

     

     
    * Use the ``GetHostedZone`` action to request information about the hosted zone. 
     
    * Use the ``ListHostedZones`` action to get a list of the hosted zones associated with the current AWS account. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DeleteHostedZone>`_    


    **Request Syntax** 
    ::

      response = client.delete_hosted_zone(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the hosted zone you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``DeleteHostedZone`` request.

        
        

        - **ChangeInfo** *(dict) --* 

          A complex type that contains the ID, the status, and the date and time of a request to delete a hosted zone.

          
          

          - **Id** *(string) --* 

            The ID of the request.

            
          

          - **Status** *(string) --* 

            The current state of the request. ``PENDING`` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

            
          

          - **SubmittedAt** *(datetime) --* 

            The date and time that the change request was submitted in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

            
          

          - **Comment** *(string) --* 

            A complex type that describes change information about changes made to your hosted zone.

             

            This element contains an ID that you use when performing a  GetChange action to get detailed information about the change.

            
      
    

  .. py:method:: delete_query_logging_config(**kwargs)

    

    Deletes a configuration for DNS query logging. If you delete a configuration, Amazon Route 53 stops sending query logs to CloudWatch Logs. Amazon Route 53 doesn't delete any logs that are already in CloudWatch Logs.

     

    For more information about DNS query logs, see  CreateQueryLoggingConfig .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DeleteQueryLoggingConfig>`_    


    **Request Syntax** 
    ::

      response = client.delete_query_logging_config(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the configuration that you want to delete. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_reusable_delegation_set(**kwargs)

    

    Deletes a reusable delegation set.

     

    .. warning::

       

      You can delete a reusable delegation set only if it isn't associated with any hosted zones.

       

     

    To verify that the reusable delegation set is not associated with any hosted zones, submit a  GetReusableDelegationSet request and specify the ID of the reusable delegation set that you want to delete.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DeleteReusableDelegationSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_reusable_delegation_set(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the reusable delegation set that you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element.

        
    

  .. py:method:: delete_traffic_policy(**kwargs)

    

    Deletes a traffic policy.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DeleteTrafficPolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_traffic_policy(
          Id='string',
          Version=123
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the traffic policy that you want to delete.

      

    
    :type Version: integer
    :param Version: **[REQUIRED]** 

      The version number of the traffic policy that you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element.

        
    

  .. py:method:: delete_traffic_policy_instance(**kwargs)

    

    Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.

     

    .. note::

       

      In the Amazon Route 53 console, traffic policy instances are known as policy records.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DeleteTrafficPolicyInstance>`_    


    **Request Syntax** 
    ::

      response = client.delete_traffic_policy_instance(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the traffic policy instance that you want to delete. 

       

      .. warning::

         

        When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element.

        
    

  .. py:method:: delete_vpc_association_authorization(**kwargs)

    

    Removes authorization to submit an ``AssociateVPCWithHostedZone`` request to associate a specified VPC with a hosted zone that was created by a different account. You must use the account that created the hosted zone to submit a ``DeleteVPCAssociationAuthorization`` request.

     

    .. warning::

       

      Sending this request only prevents the AWS account that created the VPC from associating the VPC with the Amazon Route 53 hosted zone in the future. If the VPC is already associated with the hosted zone, ``DeleteVPCAssociationAuthorization`` won't disassociate the VPC from the hosted zone. If you want to delete an existing association, use ``DisassociateVPCFromHostedZone`` .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DeleteVPCAssociationAuthorization>`_    


    **Request Syntax** 
    ::

      response = client.delete_vpc_association_authorization(
          HostedZoneId='string',
          VPC={
              'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
              'VPCId': 'string'
          }
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      When removing authorization to associate a VPC that was created by one AWS account with a hosted zone that was created with a different AWS account, the ID of the hosted zone.

      

    
    :type VPC: dict
    :param VPC: **[REQUIRED]** 

      When removing authorization to associate a VPC that was created by one AWS account with a hosted zone that was created with a different AWS account, a complex type that includes the ID and region of the VPC.

      

    
      - **VPCRegion** *(string) --* 

        (Private hosted zones only) The region in which you created an Amazon VPC.

        

      
      - **VPCId** *(string) --* 

        (Private hosted zones only) The ID of an Amazon VPC. 

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Empty response for the request.

        
    

  .. py:method:: disassociate_vpc_from_hosted_zone(**kwargs)

    

    Disassociates a VPC from a Amazon Route 53 private hosted zone. 

     

    .. note::

       

      You can't disassociate the last VPC from a private hosted zone.

       

     

    .. warning::

       

      You can't disassociate a VPC from a private hosted zone when only one VPC is associated with the hosted zone. You also can't convert a private hosted zone into a public hosted zone.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DisassociateVPCFromHostedZone>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_vpc_from_hosted_zone(
          HostedZoneId='string',
          VPC={
              'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
              'VPCId': 'string'
          },
          Comment='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the private hosted zone that you want to disassociate a VPC from.

      

    
    :type VPC: dict
    :param VPC: **[REQUIRED]** 

      A complex type that contains information about the VPC that you're disassociating from the specified hosted zone.

      

    
      - **VPCRegion** *(string) --* 

        (Private hosted zones only) The region in which you created an Amazon VPC.

        

      
      - **VPCId** *(string) --* 

        (Private hosted zones only) The ID of an Amazon VPC. 

        

      
    
    :type Comment: string
    :param Comment: 

       *Optional:* A comment about the disassociation request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the disassociate request.

        
        

        - **ChangeInfo** *(dict) --* 

          A complex type that describes the changes made to the specified private hosted zone.

          
          

          - **Id** *(string) --* 

            The ID of the request.

            
          

          - **Status** *(string) --* 

            The current state of the request. ``PENDING`` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

            
          

          - **SubmittedAt** *(datetime) --* 

            The date and time that the change request was submitted in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

            
          

          - **Comment** *(string) --* 

            A complex type that describes change information about changes made to your hosted zone.

             

            This element contains an ID that you use when performing a  GetChange action to get detailed information about the change.

            
      
    

  .. py:method:: generate_presigned_url(ClientMethod, Params=None, ExpiresIn=3600, HttpMethod=None)

        
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for
    
    :type Params: dict
    :param Params: The parameters normally passed to
        ``ClientMethod``.
    
    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
        for. By default it expires in an hour (3600 seconds)
    
    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
        default, the http method is whatever is used in the method's model.
    
    :returns: The presigned url


  .. py:method:: get_account_limit(**kwargs)

    

    Gets the specified limit for the current account, for example, the maximum number of health checks that you can create using the account.

     

    For the default limit, see `Limits <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html>`__ in the *Amazon Route 53 Developer Guide* . To request a higher limit, `open a case <https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetAccountLimit>`_    


    **Request Syntax** 
    ::

      response = client.get_account_limit(
          Type='MAX_HEALTH_CHECKS_BY_OWNER'|'MAX_HOSTED_ZONES_BY_OWNER'|'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER'|'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER'|'MAX_TRAFFIC_POLICIES_BY_OWNER'
      )
    :type Type: string
    :param Type: **[REQUIRED]** 

      The limit that you want to get. Valid values include the following:

       

       
      * **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create using the current account. 
       
      * **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create using the current account. 
       
      * **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation sets that you can create using the current account. 
       
      * **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can create using the current account. 
       
      * **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.) 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Limit': {
                'Type': 'MAX_HEALTH_CHECKS_BY_OWNER'|'MAX_HOSTED_ZONES_BY_OWNER'|'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER'|'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER'|'MAX_TRAFFIC_POLICIES_BY_OWNER',
                'Value': 123
            },
            'Count': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the requested limit. 

        
        

        - **Limit** *(dict) --* 

          The current setting for the specified limit. For example, if you specified ``MAX_HEALTH_CHECKS_BY_OWNER`` for the value of ``Type`` in the request, the value of ``Limit`` is the maximum number of health checks that you can create using the current account.

          
          

          - **Type** *(string) --* 

            The limit that you requested. Valid values include the following:

             

             
            * **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create using the current account. 
             
            * **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create using the current account. 
             
            * **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation sets that you can create using the current account. 
             
            * **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can create using the current account. 
             
            * **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.) 
             

            
          

          - **Value** *(integer) --* 

            The current value for the limit that is specified by  AccountLimit$Type .

            
      
        

        - **Count** *(integer) --* 

          The current number of entities that you have created of the specified type. For example, if you specified ``MAX_HEALTH_CHECKS_BY_OWNER`` for the value of ``Type`` in the request, the value of ``Count`` is the current number of health checks that you have created using the current account.

          
    

  .. py:method:: get_change(**kwargs)

    

    Returns the current status of a change batch request. The status is one of the following values:

     

     
    * ``PENDING`` indicates that the changes in this request have not propagated to all Amazon Route 53 DNS servers. This is the initial status of all change batch requests. 
     
    * ``INSYNC`` indicates that the changes have propagated to all Amazon Route 53 DNS servers.  
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetChange>`_    


    **Request Syntax** 
    ::

      response = client.get_change(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the change batch request. The value that you specify here is the value that ``ChangeResourceRecordSets`` returned in the ``Id`` element when you submitted the request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the ``ChangeInfo`` element.

        
        

        - **ChangeInfo** *(dict) --* 

          A complex type that contains information about the specified change batch.

          
          

          - **Id** *(string) --* 

            The ID of the request.

            
          

          - **Status** *(string) --* 

            The current state of the request. ``PENDING`` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

            
          

          - **SubmittedAt** *(datetime) --* 

            The date and time that the change request was submitted in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

            
          

          - **Comment** *(string) --* 

            A complex type that describes change information about changes made to your hosted zone.

             

            This element contains an ID that you use when performing a  GetChange action to get detailed information about the change.

            
      
    

  .. py:method:: get_checker_ip_ranges()

    

     ``GetCheckerIpRanges`` still works, but we recommend that you download ip-ranges.json, which includes IP address ranges for all AWS services. For more information, see `IP Address Ranges of Amazon Route 53 Servers <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-ip-addresses.html>`__ in the *Amazon Route 53 Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetCheckerIpRanges>`_    


    **Request Syntax** 
    ::

      response = client.get_checker_ip_ranges()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CheckerIpRanges': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CheckerIpRanges** *(list) --* 
          

          - *(string) --* 
      
    

  .. py:method:: get_geo_location(**kwargs)

    

    Gets information about whether a specified geographic location is supported for Amazon Route 53 geolocation resource record sets.

     

    Use the following syntax to determine whether a continent is supported for geolocation:

     

     ``GET /2013-04-01/geolocation?ContinentCode=*two-letter abbreviation for a continent* ``  

     

    Use the following syntax to determine whether a country is supported for geolocation:

     

     ``GET /2013-04-01/geolocation?CountryCode=*two-character country code* ``  

     

    Use the following syntax to determine whether a subdivision of a country is supported for geolocation:

     

     ``GET /2013-04-01/geolocation?CountryCode=*two-character country code* &SubdivisionCode=*subdivision code* ``  

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetGeoLocation>`_    


    **Request Syntax** 
    ::

      response = client.get_geo_location(
          ContinentCode='string',
          CountryCode='string',
          SubdivisionCode='string'
      )
    :type ContinentCode: string
    :param ContinentCode: 

      Amazon Route 53 supports the following continent codes:

       

       
      * **AF** : Africa 
       
      * **AN** : Antarctica 
       
      * **AS** : Asia 
       
      * **EU** : Europe 
       
      * **OC** : Oceania 
       
      * **NA** : North America 
       
      * **SA** : South America 
       

      

    
    :type CountryCode: string
    :param CountryCode: 

      Amazon Route 53 uses the two-letter country codes that are specified in `ISO standard 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ .

      

    
    :type SubdivisionCode: string
    :param SubdivisionCode: 

      Amazon Route 53 uses the one- to three-letter subdivision codes that are specified in `ISO standard 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ . Amazon Route 53 doesn't support subdivision codes for all countries. If you specify ``SubdivisionCode`` , you must also specify ``CountryCode`` . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GeoLocationDetails': {
                'ContinentCode': 'string',
                'ContinentName': 'string',
                'CountryCode': 'string',
                'CountryName': 'string',
                'SubdivisionCode': 'string',
                'SubdivisionName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the specified geolocation code.

        
        

        - **GeoLocationDetails** *(dict) --* 

          A complex type that contains the codes and full continent, country, and subdivision names for the specified geolocation code.

          
          

          - **ContinentCode** *(string) --* 

            The two-letter code for the continent.

            
          

          - **ContinentName** *(string) --* 

            The full name of the continent.

            
          

          - **CountryCode** *(string) --* 

            The two-letter code for the country.

            
          

          - **CountryName** *(string) --* 

            The name of the country.

            
          

          - **SubdivisionCode** *(string) --* 

            The code for the subdivision, for example, a state in the United States or a province in Canada.

            
          

          - **SubdivisionName** *(string) --* 

            The full name of the subdivision, for example, a state in the United States or a province in Canada.

            
      
    

  .. py:method:: get_health_check(**kwargs)

    

    Gets information about a specified health check.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetHealthCheck>`_    


    **Request Syntax** 
    ::

      response = client.get_health_check(
          HealthCheckId='string'
      )
    :type HealthCheckId: string
    :param HealthCheckId: **[REQUIRED]** 

      The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthCheck': {
                'Id': 'string',
                'CallerReference': 'string',
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                },
                'HealthCheckConfig': {
                    'IPAddress': 'string',
                    'Port': 123,
                    'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                    'ResourcePath': 'string',
                    'FullyQualifiedDomainName': 'string',
                    'SearchString': 'string',
                    'RequestInterval': 123,
                    'FailureThreshold': 123,
                    'MeasureLatency': True|False,
                    'Inverted': True|False,
                    'HealthThreshold': 123,
                    'ChildHealthChecks': [
                        'string',
                    ],
                    'EnableSNI': True|False,
                    'Regions': [
                        'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                    ],
                    'AlarmIdentifier': {
                        'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                        'Name': 'string'
                    },
                    'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
                },
                'HealthCheckVersion': 123,
                'CloudWatchAlarmConfiguration': {
                    'EvaluationPeriods': 123,
                    'Threshold': 123.0,
                    'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                    'Period': 123,
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``GetHealthCheck`` request.

        
        

        - **HealthCheck** *(dict) --* 

          A complex type that contains information about one health check that is associated with the current AWS account.

          
          

          - **Id** *(string) --* 

            The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. 

            
          

          - **CallerReference** *(string) --* 

            A unique string that you specified when you created the health check.

            
          

          - **LinkedService** *(dict) --* 

            If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can't edit or delete it using Amazon Route 53. 

            
            

            - **ServicePrincipal** *(string) --* 

              If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
            

            - **Description** *(string) --* 

              If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
        
          

          - **HealthCheckConfig** *(dict) --* 

            A complex type that contains detailed information about one health check.

            
            

            - **IPAddress** *(string) --* 

              The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Amazon Route 53 then checks the health of the endpoint.

               

              Use one of the following formats for the value of ``IPAddress`` : 

               

               
              * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
               
              * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
               

               

              If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.

               

              For more information, see  HealthCheckConfig$FullyQualifiedDomainName .

               

              Constraints: Amazon Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

               

               
              * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
               
              * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
               
              * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
               

               

              When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

              
            

            - **Port** *(integer) --* 

              The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

              
            

            - **Type** *(string) --* 

              The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

               

              .. warning::

                 

                You can't change the value of ``Type`` after you create a health check.

                 

               

              You can create the following types of health checks:

               

               
              * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
               
              * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

              .. warning::

                 If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

               
               
              * **HTTP_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
               
              * **HTTPS_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
               
              * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
               
              * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .  
               
              * **CALCULATED** : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .  
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

              
            

            - **ResourcePath** *(string) --* 

              The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. 

              
            

            - **FullyQualifiedDomainName** *(string) --* 

              Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

               

               **If you specify a value for**  ``IPAddress`` :

               

              Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks.

               

              When Amazon Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

               

               
              * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.  
               
              * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
               
              * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Amazon Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. 
               

               

              If you don't specify a value for ``FullyQualifiedDomainName`` , Amazon Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

               

               **If you don't specify a value for ``IPAddress`` ** :

               

              Amazon Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Amazon Route 53 then checks the health of the endpoint.

               

              .. note::

                 

                If you don't specify a value for ``IPAddress`` , Amazon Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

                 

               

              If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

               

              .. warning::

                 

                In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

                 

               

              In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Amazon Route 53 doesn't pass a ``Host`` header.

              
            

            - **SearchString** *(string) --* 

              If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.

               

              Amazon Route 53 considers case when searching for ``SearchString`` in the response body. 

              
            

            - **RequestInterval** *(integer) --* 

              The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Amazon Route 53 health checker makes requests at this interval.

               

              .. warning::

                 

                You can't change the value of ``RequestInterval`` after you create a health check.

                 

               

              If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

              
            

            - **FailureThreshold** *(integer) --* 

              The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

              
            

            - **MeasureLatency** *(boolean) --* 

              Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Amazon Route 53 console.

               

              .. warning::

                 

                You can't change the value of ``MeasureLatency`` after you create a health check.

                 

              
            

            - **Inverted** *(boolean) --* 

              Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

              
            

            - **HealthThreshold** *(integer) --* 

              The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.

               

              Note the following:

               

               
              * If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy. 
               
              * If you specify ``0`` , Amazon Route 53 always considers this health check to be healthy. 
               

              
            

            - **ChildHealthChecks** *(list) --* 

              (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

              
              

              - *(string) --* 
          
            

            - **EnableSNI** *(boolean) --* 

              Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

               

              Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

               

              The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

              
            

            - **Regions** *(list) --* 

              A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

               

              If you don't specify any regions, Amazon Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .

               

              If you update a health check to remove a region that has been performing health checks, Amazon Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions). 

              
              

              - *(string) --* 
          
            

            - **AlarmIdentifier** *(dict) --* 

              A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

              
              

              - **Region** *(string) --* 

                A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                 

                For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

                
              

              - **Name** *(string) --* 

                The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                
          
            

            - **InsufficientDataHealthStatus** *(string) --* 

              When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

               

               
              * ``Healthy`` : Amazon Route 53 considers the health check to be healthy. 
               
              * ``Unhealthy`` : Amazon Route 53 considers the health check to be unhealthy. 
               
              * ``LastKnownStatus`` : Amazon Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
               

              
        
          

          - **HealthCheckVersion** *(integer) --* 

            The version of the health check. You can optionally pass this value in a call to ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

            
          

          - **CloudWatchAlarmConfiguration** *(dict) --* 

            A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

            
            

            - **EvaluationPeriods** *(integer) --* 

              For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

              
            

            - **Threshold** *(float) --* 

              For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

              
            

            - **ComparisonOperator** *(string) --* 

              For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

              
            

            - **Period** *(integer) --* 

              For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

              
            

            - **MetricName** *(string) --* 

              The name of the CloudWatch metric that the alarm is associated with.

              
            

            - **Namespace** *(string) --* 

              The namespace of the metric that the alarm is associated with. For more information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

              
            

            - **Statistic** *(string) --* 

              For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

              
            

            - **Dimensions** *(list) --* 

              For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

              
              

              - *(dict) --* 

                For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

                
                

                - **Name** *(string) --* 

                  For the metric that the CloudWatch alarm is associated with, the name of one dimension.

                  
                

                - **Value** *(string) --* 

                  For the metric that the CloudWatch alarm is associated with, the value of one dimension.

                  
            
          
        
      
    

  .. py:method:: get_health_check_count()

    

    Retrieves the number of health checks that are associated with the current AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetHealthCheckCount>`_    


    **Request Syntax** 
    ::

      response = client.get_health_check_count()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthCheckCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``GetHealthCheckCount`` request.

        
        

        - **HealthCheckCount** *(integer) --* 

          The number of health checks associated with the current AWS account.

          
    

  .. py:method:: get_health_check_last_failure_reason(**kwargs)

    

    Gets the reason that a specified health check failed most recently.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetHealthCheckLastFailureReason>`_    


    **Request Syntax** 
    ::

      response = client.get_health_check_last_failure_reason(
          HealthCheckId='string'
      )
    :type HealthCheckId: string
    :param HealthCheckId: **[REQUIRED]** 

      The ID for the health check for which you want the last failure reason. When you created the health check, ``CreateHealthCheck`` returned the ID in the response, in the ``HealthCheckId`` element.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthCheckObservations': [
                {
                    'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                    'IPAddress': 'string',
                    'StatusReport': {
                        'Status': 'string',
                        'CheckedTime': datetime(2015, 1, 1)
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``GetHealthCheckLastFailureReason`` request.

        
        

        - **HealthCheckObservations** *(list) --* 

          A list that contains one ``Observation`` element for each Amazon Route 53 health checker that is reporting a last failure reason. 

          
          

          - *(dict) --* 

            A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker.

            
            

            - **Region** *(string) --* 

              The region of the Amazon Route 53 health checker that provided the status in ``StatusReport`` .

              
            

            - **IPAddress** *(string) --* 

              The IP address of the Amazon Route 53 health checker that provided the failure reason in ``StatusReport`` .

              
            

            - **StatusReport** *(dict) --* 

              A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.

              
              

              - **Status** *(string) --* 

                A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.

                
              

              - **CheckedTime** *(datetime) --* 

                The date and time that the health checker performed the health check in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

                
          
        
      
    

  .. py:method:: get_health_check_status(**kwargs)

    

    Gets status of a specified health check. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetHealthCheckStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_health_check_status(
          HealthCheckId='string'
      )
    :type HealthCheckId: string
    :param HealthCheckId: **[REQUIRED]** 

      The ID for the health check that you want the current status for. When you created the health check, ``CreateHealthCheck`` returned the ID in the response, in the ``HealthCheckId`` element.

       

      .. note::

         

        If you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use ``GetHealthCheckStatus`` to get the status of a calculated health check.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthCheckObservations': [
                {
                    'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                    'IPAddress': 'string',
                    'StatusReport': {
                        'Status': 'string',
                        'CheckedTime': datetime(2015, 1, 1)
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``GetHealthCheck`` request.

        
        

        - **HealthCheckObservations** *(list) --* 

          A list that contains one ``HealthCheckObservation`` element for each Amazon Route 53 health checker that is reporting a status about the health check endpoint.

          
          

          - *(dict) --* 

            A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker.

            
            

            - **Region** *(string) --* 

              The region of the Amazon Route 53 health checker that provided the status in ``StatusReport`` .

              
            

            - **IPAddress** *(string) --* 

              The IP address of the Amazon Route 53 health checker that provided the failure reason in ``StatusReport`` .

              
            

            - **StatusReport** *(dict) --* 

              A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.

              
              

              - **Status** *(string) --* 

                A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.

                
              

              - **CheckedTime** *(datetime) --* 

                The date and time that the health checker performed the health check in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751 UTC.

                
          
        
      
    

  .. py:method:: get_hosted_zone(**kwargs)

    

    Gets information about a specified hosted zone including the four name servers assigned to the hosted zone.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetHostedZone>`_    


    **Request Syntax** 
    ::

      response = client.get_hosted_zone(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the hosted zone that you want to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZone': {
                'Id': 'string',
                'Name': 'string',
                'CallerReference': 'string',
                'Config': {
                    'Comment': 'string',
                    'PrivateZone': True|False
                },
                'ResourceRecordSetCount': 123,
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                }
            },
            'DelegationSet': {
                'Id': 'string',
                'CallerReference': 'string',
                'NameServers': [
                    'string',
                ]
            },
            'VPCs': [
                {
                    'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
                    'VPCId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contain the response to a ``GetHostedZone`` request.

        
        

        - **HostedZone** *(dict) --* 

          A complex type that contains general information about the specified hosted zone.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the hosted zone when you created it.

            
          

          - **Name** *(string) --* 

            The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

             

            For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see  CreateHostedZone .

            
          

          - **CallerReference** *(string) --* 

            The value that you specified for ``CallerReference`` when you created the hosted zone.

            
          

          - **Config** *(dict) --* 

            A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and ``Comment`` elements don't appear in the response.

            
            

            - **Comment** *(string) --* 

              Any comments that you want to include about the hosted zone.

              
            

            - **PrivateZone** *(boolean) --* 

              A value that indicates whether this is a private hosted zone.

              
        
          

          - **ResourceRecordSetCount** *(integer) --* 

            The number of resource record sets in the hosted zone.

            
          

          - **LinkedService** *(dict) --* 

            If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Amazon Route 53. 

            
            

            - **ServicePrincipal** *(string) --* 

              If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
            

            - **Description** *(string) --* 

              If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
        
      
        

        - **DelegationSet** *(dict) --* 

          A complex type that lists the Amazon Route 53 name servers for the specified hosted zone.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigns to a reusable delegation set.

            
          

          - **CallerReference** *(string) --* 

            The value that you specified for ``CallerReference`` when you created the reusable delegation set.

            
          

          - **NameServers** *(list) --* 

            A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

            
            

            - *(string) --* 
        
      
        

        - **VPCs** *(list) --* 

          A complex type that contains information about the VPCs that are associated with the specified hosted zone.

          
          

          - *(dict) --* 

            (Private hosted zones only) A complex type that contains information about an Amazon VPC.

            
            

            - **VPCRegion** *(string) --* 

              (Private hosted zones only) The region in which you created an Amazon VPC.

              
            

            - **VPCId** *(string) --* 

              (Private hosted zones only) The ID of an Amazon VPC. 

              
        
      
    

  .. py:method:: get_hosted_zone_count()

    

    Retrieves the number of hosted zones that are associated with the current AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetHostedZoneCount>`_    


    **Request Syntax** 
    ::

      response = client.get_hosted_zone_count()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZoneCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``GetHostedZoneCount`` request.

        
        

        - **HostedZoneCount** *(integer) --* 

          The total number of public and private hosted zones that are associated with the current AWS account.

          
    

  .. py:method:: get_hosted_zone_limit(**kwargs)

    

    Gets the specified limit for a specified hosted zone, for example, the maximum number of records that you can create in the hosted zone. 

     

    For the default limit, see `Limits <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html>`__ in the *Amazon Route 53 Developer Guide* . To request a higher limit, `open a case <https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetHostedZoneLimit>`_    


    **Request Syntax** 
    ::

      response = client.get_hosted_zone_limit(
          Type='MAX_RRSETS_BY_ZONE'|'MAX_VPCS_ASSOCIATED_BY_ZONE',
          HostedZoneId='string'
      )
    :type Type: string
    :param Type: **[REQUIRED]** 

      The limit that you want to get. Valid values include the following:

       

       
      * **MAX_RRSETS_BY_ZONE** : The maximum number of records that you can create in the specified hosted zone. 
       
      * **MAX_VPCS_ASSOCIATED_BY_TYPE** : The maximum number of Amazon VPCs that you can associate with the specified private hosted zone. 
       

      

    
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone that you want to get a limit for.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Limit': {
                'Type': 'MAX_RRSETS_BY_ZONE'|'MAX_VPCS_ASSOCIATED_BY_ZONE',
                'Value': 123
            },
            'Count': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the requested limit. 

        
        

        - **Limit** *(dict) --* 

          The current setting for the specified limit. For example, if you specified ``MAX_RRSETS_BY_ZONE`` for the value of ``Type`` in the request, the value of ``Limit`` is the maximum number of records that you can create in the specified hosted zone.

          
          

          - **Type** *(string) --* 

            The limit that you requested. Valid values include the following:

             

             
            * **MAX_RRSETS_BY_ZONE** : The maximum number of records that you can create in the specified hosted zone. 
             
            * **MAX_VPCS_ASSOCIATED_BY_TYPE** : The maximum number of Amazon VPCs that you can associate with the specified private hosted zone. 
             

            
          

          - **Value** *(integer) --* 

            The current value for the limit that is specified by ``Type`` .

            
      
        

        - **Count** *(integer) --* 

          The current number of entities that you have created of the specified type. For example, if you specified ``MAX_RRSETS_BY_ZONE`` for the value of ``Type`` in the request, the value of ``Count`` is the current number of records that you have created in the specified hosted zone.

          
    

  .. py:method:: get_paginator(operation_name)

        
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name.  This is the same name
        as the method name on the client.  For example, if the
        method name is ``create_foo``, and you'd normally invoke the
        operation as ``client.create_foo(**kwargs)``, if the
        ``create_foo`` operation can be paginated, you can use the
        call ``client.get_paginator("create_foo")``.
    
    :raise OperationNotPageableError: Raised if the operation is not
        pageable.  You can use the ``client.can_paginate`` method to
        check if an operation is pageable.
    
    :rtype: L{botocore.paginate.Paginator}
    :return: A paginator object.


  .. py:method:: get_query_logging_config(**kwargs)

    

    Gets information about a specified configuration for DNS query logging.

     

    For more information about DNS query logs, see  CreateQueryLoggingConfig and `Logging DNS Queries <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetQueryLoggingConfig>`_    


    **Request Syntax** 
    ::

      response = client.get_query_logging_config(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the configuration for DNS query logging that you want to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'QueryLoggingConfig': {
                'Id': 'string',
                'HostedZoneId': 'string',
                'CloudWatchLogsLogGroupArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryLoggingConfig** *(dict) --* 

          A complex type that contains information about the query logging configuration that you specified in a  GetQueryLoggingConfig request.

          
          

          - **Id** *(string) --* 

            The ID for a configuration for DNS query logging.

            
          

          - **HostedZoneId** *(string) --* 

            The ID of the hosted zone that CloudWatch Logs is logging queries for. 

            
          

          - **CloudWatchLogsLogGroupArn** *(string) --* 

            The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.

            
      
    

  .. py:method:: get_reusable_delegation_set(**kwargs)

    

    Retrieves information about a specified reusable delegation set, including the four name servers that are assigned to the delegation set.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetReusableDelegationSet>`_    


    **Request Syntax** 
    ::

      response = client.get_reusable_delegation_set(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the reusable delegation set that you want to get a list of name servers for.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DelegationSet': {
                'Id': 'string',
                'CallerReference': 'string',
                'NameServers': [
                    'string',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to the ``GetReusableDelegationSet`` request.

        
        

        - **DelegationSet** *(dict) --* 

          A complex type that contains information about the reusable delegation set.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigns to a reusable delegation set.

            
          

          - **CallerReference** *(string) --* 

            The value that you specified for ``CallerReference`` when you created the reusable delegation set.

            
          

          - **NameServers** *(list) --* 

            A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

            
            

            - *(string) --* 
        
      
    

  .. py:method:: get_reusable_delegation_set_limit(**kwargs)

    

    Gets the maximum number of hosted zones that you can associate with the specified reusable delegation set.

     

    For the default limit, see `Limits <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html>`__ in the *Amazon Route 53 Developer Guide* . To request a higher limit, `open a case <https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetReusableDelegationSetLimit>`_    


    **Request Syntax** 
    ::

      response = client.get_reusable_delegation_set_limit(
          Type='MAX_ZONES_BY_REUSABLE_DELEGATION_SET',
          DelegationSetId='string'
      )
    :type Type: string
    :param Type: **[REQUIRED]** 

      Specify ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.

      

    
    :type DelegationSetId: string
    :param DelegationSetId: **[REQUIRED]** 

      The ID of the delegation set that you want to get the limit for.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Limit': {
                'Type': 'MAX_ZONES_BY_REUSABLE_DELEGATION_SET',
                'Value': 123
            },
            'Count': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the requested limit. 

        
        

        - **Limit** *(dict) --* 

          The current setting for the limit on hosted zones that you can associate with the specified reusable delegation set.

          
          

          - **Type** *(string) --* 

            The limit that you requested: ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` , the maximum number of hosted zones that you can associate with the specified reusable delegation set.

            
          

          - **Value** *(integer) --* 

            The current value for the ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` limit.

            
      
        

        - **Count** *(integer) --* 

          The current number of hosted zones that you can associate with the specified reusable delegation set.

          
    

  .. py:method:: get_traffic_policy(**kwargs)

    

    Gets information about a specific traffic policy version.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetTrafficPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_traffic_policy(
          Id='string',
          Version=123
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the traffic policy that you want to get information about.

      

    
    :type Version: integer
    :param Version: **[REQUIRED]** 

      The version number of the traffic policy that you want to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicy': {
                'Id': 'string',
                'Version': 123,
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                'Document': 'string',
                'Comment': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **TrafficPolicy** *(dict) --* 

          A complex type that contains settings for the specified traffic policy.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to a traffic policy when you created it.

            
          

          - **Version** *(integer) --* 

            The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of ``Version`` is always 1.

            
          

          - **Name** *(string) --* 

            The name that you specified when you created the traffic policy.

            
          

          - **Type** *(string) --* 

            The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

            
          

          - **Document** *(string) --* 

            The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the JSON format, see `Traffic Policy Document Format <http://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__ .

            
          

          - **Comment** *(string) --* 

            The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

            
      
    

  .. py:method:: get_traffic_policy_instance(**kwargs)

    

    Gets information about a specified traffic policy instance.

     

    .. note::

       

      After you submit a ``CreateTrafficPolicyInstance`` or an ``UpdateTrafficPolicyInstance`` request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the ``State`` response element.

       

     

    .. note::

       

      In the Amazon Route 53 console, traffic policy instances are known as policy records.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetTrafficPolicyInstance>`_    


    **Request Syntax** 
    ::

      response = client.get_traffic_policy_instance(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the traffic policy instance that you want to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicyInstance': {
                'Id': 'string',
                'HostedZoneId': 'string',
                'Name': 'string',
                'TTL': 123,
                'State': 'string',
                'Message': 'string',
                'TrafficPolicyId': 'string',
                'TrafficPolicyVersion': 123,
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains information about the resource record sets that Amazon Route 53 created based on a specified traffic policy.

        
        

        - **TrafficPolicyInstance** *(dict) --* 

          A complex type that contains settings for the traffic policy instance.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the new traffic policy instance.

            
          

          - **HostedZoneId** *(string) --* 

            The ID of the hosted zone that Amazon Route 53 created resource record sets in.

            
          

          - **Name** *(string) --* 

            The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance. 

            
          

          - **TTL** *(integer) --* 

            The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

            
          

          - **State** *(string) --* 

            The value of ``State`` is one of the following values:

              Applied  

            Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Amazon Route 53 edge locations.

              Creating  

            Amazon Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

              Failed  

            Amazon Route 53 wasn't able to create or update the resource record sets. When the value of ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to fail.

              
          

          - **Message** *(string) --* 

            If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is another value, ``Message`` is empty.

            
          

          - **TrafficPolicyId** *(string) --* 

            The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

            
          

          - **TrafficPolicyVersion** *(integer) --* 

            The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

            
          

          - **TrafficPolicyType** *(string) --* 

            The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance. 

            
      
    

  .. py:method:: get_traffic_policy_instance_count()

    

    Gets the number of traffic policy instances that are associated with the current AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetTrafficPolicyInstanceCount>`_    


    **Request Syntax** 
    ::

      response = client.get_traffic_policy_instance_count()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicyInstanceCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains information about the resource record sets that Amazon Route 53 created based on a specified traffic policy.

        
        

        - **TrafficPolicyInstanceCount** *(integer) --* 

          The number of traffic policy instances that are associated with the current AWS account.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_geo_locations(**kwargs)

    

    Retrieves a list of supported geo locations.

     

    Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListGeoLocations>`_    


    **Request Syntax** 
    ::

      response = client.list_geo_locations(
          StartContinentCode='string',
          StartCountryCode='string',
          StartSubdivisionCode='string',
          MaxItems='string'
      )
    :type StartContinentCode: string
    :param StartContinentCode: 

      The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if ``IsTruncated`` is true, and if ``NextContinentCode`` from the previous response has a value, enter that value in ``StartContinentCode`` to return the next page of results.

       

      Include ``StartContinentCode`` only if you want to list continents. Don't include ``StartContinentCode`` when you're listing countries or countries with their subdivisions.

      

    
    :type StartCountryCode: string
    :param StartCountryCode: 

      The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if ``IsTruncated`` is ``true`` , and if ``NextCountryCode`` from the previous response has a value, enter that value in ``StartCountryCode`` to return the next page of results.

       

      Amazon Route 53 uses the two-letter country codes that are specified in `ISO standard 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ .

      

    
    :type StartSubdivisionCode: string
    :param StartSubdivisionCode: 

      The code for the subdivision (for example, state or province) with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if ``IsTruncated`` is ``true`` , and if ``NextSubdivisionCode`` from the previous response has a value, enter that value in ``StartSubdivisionCode`` to return the next page of results.

       

      To list subdivisions of a country, you must include both ``StartCountryCode`` and ``StartSubdivisionCode`` .

      

    
    :type MaxItems: string
    :param MaxItems: 

      (Optional) The maximum number of geolocations to be included in the response body for this request. If more than ``MaxItems`` geolocations remain to be listed, then the value of the ``IsTruncated`` element in the response is ``true`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GeoLocationDetailsList': [
                {
                    'ContinentCode': 'string',
                    'ContinentName': 'string',
                    'CountryCode': 'string',
                    'CountryName': 'string',
                    'SubdivisionCode': 'string',
                    'SubdivisionName': 'string'
                },
            ],
            'IsTruncated': True|False,
            'NextContinentCode': 'string',
            'NextCountryCode': 'string',
            'NextSubdivisionCode': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type containing the response information for the request.

        
        

        - **GeoLocationDetailsList** *(list) --* 

          A complex type that contains one ``GeoLocationDetails`` element for each location that Amazon Route 53 supports for geolocation.

          
          

          - *(dict) --* 

            A complex type that contains the codes and full continent, country, and subdivision names for the specified ``geolocation`` code.

            
            

            - **ContinentCode** *(string) --* 

              The two-letter code for the continent.

              
            

            - **ContinentName** *(string) --* 

              The full name of the continent.

              
            

            - **CountryCode** *(string) --* 

              The two-letter code for the country.

              
            

            - **CountryName** *(string) --* 

              The name of the country.

              
            

            - **SubdivisionCode** *(string) --* 

              The code for the subdivision, for example, a state in the United States or a province in Canada.

              
            

            - **SubdivisionName** *(string) --* 

              The full name of the subdivision, for example, a state in the United States or a province in Canada.

              
        
      
        

        - **IsTruncated** *(boolean) --* 

          A value that indicates whether more locations remain to be listed after the last location in this response. If so, the value of ``IsTruncated`` is ``true`` . To get more values, submit another request and include the values of ``NextContinentCode`` , ``NextCountryCode`` , and ``NextSubdivisionCode`` in the ``StartContinentCode`` , ``StartCountryCode`` , and ``StartSubdivisionCode`` , as applicable.

          
        

        - **NextContinentCode** *(string) --* 

          If ``IsTruncated`` is ``true`` , you can make a follow-up request to display more locations. Enter the value of ``NextContinentCode`` in the ``StartContinentCode`` parameter in another ``ListGeoLocations`` request.

          
        

        - **NextCountryCode** *(string) --* 

          If ``IsTruncated`` is ``true`` , you can make a follow-up request to display more locations. Enter the value of ``NextCountryCode`` in the ``StartCountryCode`` parameter in another ``ListGeoLocations`` request.

          
        

        - **NextSubdivisionCode** *(string) --* 

          If ``IsTruncated`` is ``true`` , you can make a follow-up request to display more locations. Enter the value of ``NextSubdivisionCode`` in the ``StartSubdivisionCode`` parameter in another ``ListGeoLocations`` request.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for ``MaxItems`` in the request.

          
    

  .. py:method:: list_health_checks(**kwargs)

    

    Retrieve a list of the health checks that are associated with the current AWS account. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHealthChecks>`_    


    **Request Syntax** 
    ::

      response = client.list_health_checks(
          Marker='string',
          MaxItems='string'
      )
    :type Marker: string
    :param Marker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more health checks. To get another group, submit another ``ListHealthChecks`` request. 

       

      For the value of ``marker`` , specify the value of ``NextMarker`` from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more health checks to get.

      

    
    :type MaxItems: string
    :param MaxItems: 

      The maximum number of health checks that you want ``ListHealthChecks`` to return in response to the current request. Amazon Route 53 returns a maximum of 100 items. If you set ``MaxItems`` to a value greater than 100, Amazon Route 53 returns only the first 100 health checks. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthChecks': [
                {
                    'Id': 'string',
                    'CallerReference': 'string',
                    'LinkedService': {
                        'ServicePrincipal': 'string',
                        'Description': 'string'
                    },
                    'HealthCheckConfig': {
                        'IPAddress': 'string',
                        'Port': 123,
                        'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                        'ResourcePath': 'string',
                        'FullyQualifiedDomainName': 'string',
                        'SearchString': 'string',
                        'RequestInterval': 123,
                        'FailureThreshold': 123,
                        'MeasureLatency': True|False,
                        'Inverted': True|False,
                        'HealthThreshold': 123,
                        'ChildHealthChecks': [
                            'string',
                        ],
                        'EnableSNI': True|False,
                        'Regions': [
                            'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                        ],
                        'AlarmIdentifier': {
                            'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                            'Name': 'string'
                        },
                        'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
                    },
                    'HealthCheckVersion': 123,
                    'CloudWatchAlarmConfiguration': {
                        'EvaluationPeriods': 123,
                        'Threshold': 123.0,
                        'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                        'Period': 123,
                        'MetricName': 'string',
                        'Namespace': 'string',
                        'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
            ],
            'Marker': 'string',
            'IsTruncated': True|False,
            'NextMarker': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``ListHealthChecks`` request.

        
        

        - **HealthChecks** *(list) --* 

          A complex type that contains one ``HealthCheck`` element for each health check that is associated with the current AWS account.

          
          

          - *(dict) --* 

            A complex type that contains information about one health check that is associated with the current AWS account.

            
            

            - **Id** *(string) --* 

              The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. 

              
            

            - **CallerReference** *(string) --* 

              A unique string that you specified when you created the health check.

              
            

            - **LinkedService** *(dict) --* 

              If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can't edit or delete it using Amazon Route 53. 

              
              

              - **ServicePrincipal** *(string) --* 

                If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
              

              - **Description** *(string) --* 

                If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
          
            

            - **HealthCheckConfig** *(dict) --* 

              A complex type that contains detailed information about one health check.

              
              

              - **IPAddress** *(string) --* 

                The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Amazon Route 53 then checks the health of the endpoint.

                 

                Use one of the following formats for the value of ``IPAddress`` : 

                 

                 
                * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
                 
                * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
                 

                 

                If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.

                 

                For more information, see  HealthCheckConfig$FullyQualifiedDomainName .

                 

                Constraints: Amazon Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

                 

                 
                * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
                 
                * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
                 
                * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
                 

                 

                When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

                
              

              - **Port** *(integer) --* 

                The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

                
              

              - **Type** *(string) --* 

                The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

                 

                .. warning::

                   

                  You can't change the value of ``Type`` after you create a health check.

                   

                 

                You can create the following types of health checks:

                 

                 
                * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
                 
                * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

                .. warning::

                   If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

                 
                 
                * **HTTP_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
                 
                * **HTTPS_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
                 
                * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
                 
                * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .  
                 
                * **CALCULATED** : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .  
                 

                 

                For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

                
              

              - **ResourcePath** *(string) --* 

                The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. 

                
              

              - **FullyQualifiedDomainName** *(string) --* 

                Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

                 

                 **If you specify a value for**  ``IPAddress`` :

                 

                Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks.

                 

                When Amazon Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

                 

                 
                * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.  
                 
                * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
                 
                * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Amazon Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. 
                 

                 

                If you don't specify a value for ``FullyQualifiedDomainName`` , Amazon Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

                 

                 **If you don't specify a value for ``IPAddress`` ** :

                 

                Amazon Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Amazon Route 53 then checks the health of the endpoint.

                 

                .. note::

                   

                  If you don't specify a value for ``IPAddress`` , Amazon Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

                   

                 

                If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

                 

                .. warning::

                   

                  In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

                   

                 

                In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Amazon Route 53 doesn't pass a ``Host`` header.

                
              

              - **SearchString** *(string) --* 

                If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.

                 

                Amazon Route 53 considers case when searching for ``SearchString`` in the response body. 

                
              

              - **RequestInterval** *(integer) --* 

                The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Amazon Route 53 health checker makes requests at this interval.

                 

                .. warning::

                   

                  You can't change the value of ``RequestInterval`` after you create a health check.

                   

                 

                If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

                
              

              - **FailureThreshold** *(integer) --* 

                The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

                 

                If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

                
              

              - **MeasureLatency** *(boolean) --* 

                Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Amazon Route 53 console.

                 

                .. warning::

                   

                  You can't change the value of ``MeasureLatency`` after you create a health check.

                   

                
              

              - **Inverted** *(boolean) --* 

                Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

                
              

              - **HealthThreshold** *(integer) --* 

                The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.

                 

                Note the following:

                 

                 
                * If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy. 
                 
                * If you specify ``0`` , Amazon Route 53 always considers this health check to be healthy. 
                 

                
              

              - **ChildHealthChecks** *(list) --* 

                (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

                
                

                - *(string) --* 
            
              

              - **EnableSNI** *(boolean) --* 

                Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

                 

                Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

                 

                The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

                
              

              - **Regions** *(list) --* 

                A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

                 

                If you don't specify any regions, Amazon Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .

                 

                If you update a health check to remove a region that has been performing health checks, Amazon Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions). 

                
                

                - *(string) --* 
            
              

              - **AlarmIdentifier** *(dict) --* 

                A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                
                

                - **Region** *(string) --* 

                  A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                   

                  For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

                  
                

                - **Name** *(string) --* 

                  The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                  
            
              

              - **InsufficientDataHealthStatus** *(string) --* 

                When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

                 

                 
                * ``Healthy`` : Amazon Route 53 considers the health check to be healthy. 
                 
                * ``Unhealthy`` : Amazon Route 53 considers the health check to be unhealthy. 
                 
                * ``LastKnownStatus`` : Amazon Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
                 

                
          
            

            - **HealthCheckVersion** *(integer) --* 

              The version of the health check. You can optionally pass this value in a call to ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

              
            

            - **CloudWatchAlarmConfiguration** *(dict) --* 

              A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

              
              

              - **EvaluationPeriods** *(integer) --* 

                For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

                
              

              - **Threshold** *(float) --* 

                For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

                
              

              - **ComparisonOperator** *(string) --* 

                For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

                
              

              - **Period** *(integer) --* 

                For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

                
              

              - **MetricName** *(string) --* 

                The name of the CloudWatch metric that the alarm is associated with.

                
              

              - **Namespace** *(string) --* 

                The namespace of the metric that the alarm is associated with. For more information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

                
              

              - **Statistic** *(string) --* 

                For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

                
              

              - **Dimensions** *(list) --* 

                For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

                
                

                - *(dict) --* 

                  For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

                  
                  

                  - **Name** *(string) --* 

                    For the metric that the CloudWatch alarm is associated with, the name of one dimension.

                    
                  

                  - **Value** *(string) --* 

                    For the metric that the CloudWatch alarm is associated with, the value of one dimension.

                    
              
            
          
        
      
        

        - **Marker** *(string) --* 

          For the second and subsequent calls to ``ListHealthChecks`` , ``Marker`` is the value that you specified for the ``marker`` parameter in the previous request.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more health checks to be listed. If the response was truncated, you can get the next group of health checks by submitting another ``ListHealthChecks`` request and specifying the value of ``NextMarker`` in the ``marker`` parameter.

          
        

        - **NextMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , the value of ``NextMarker`` identifies the first health check that Amazon Route 53 returns if you submit another ``ListHealthChecks`` request and specify the value of ``NextMarker`` in the ``marker`` parameter.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``maxitems`` parameter in the call to ``ListHealthChecks`` that produced the current response.

          
    

  .. py:method:: list_hosted_zones(**kwargs)

    

    Retrieves a list of the public and private hosted zones that are associated with the current AWS account. The response includes a ``HostedZones`` child element for each hosted zone.

     

    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of hosted zones, you can use the ``maxitems`` parameter to list them in groups of up to 100.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHostedZones>`_    


    **Request Syntax** 
    ::

      response = client.list_hosted_zones(
          Marker='string',
          MaxItems='string',
          DelegationSetId='string'
      )
    :type Marker: string
    :param Marker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more hosted zones. To get more hosted zones, submit another ``ListHostedZones`` request. 

       

      For the value of ``marker`` , specify the value of ``NextMarker`` from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more hosted zones to get.

      

    
    :type MaxItems: string
    :param MaxItems: 

      (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than ``maxitems`` hosted zones, the value of ``IsTruncated`` in the response is ``true`` , and the value of ``NextMarker`` is the hosted zone ID of the first hosted zone that Amazon Route 53 will return if you submit another request.

      

    
    :type DelegationSetId: string
    :param DelegationSetId: 

      If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZones': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'CallerReference': 'string',
                    'Config': {
                        'Comment': 'string',
                        'PrivateZone': True|False
                    },
                    'ResourceRecordSetCount': 123,
                    'LinkedService': {
                        'ServicePrincipal': 'string',
                        'Description': 'string'
                    }
                },
            ],
            'Marker': 'string',
            'IsTruncated': True|False,
            'NextMarker': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **HostedZones** *(list) --* 

          A complex type that contains general information about the hosted zone.

          
          

          - *(dict) --* 

            A complex type that contains general information about the hosted zone.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the hosted zone when you created it.

              
            

            - **Name** *(string) --* 

              The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

               

              For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see  CreateHostedZone .

              
            

            - **CallerReference** *(string) --* 

              The value that you specified for ``CallerReference`` when you created the hosted zone.

              
            

            - **Config** *(dict) --* 

              A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and ``Comment`` elements don't appear in the response.

              
              

              - **Comment** *(string) --* 

                Any comments that you want to include about the hosted zone.

                
              

              - **PrivateZone** *(boolean) --* 

                A value that indicates whether this is a private hosted zone.

                
          
            

            - **ResourceRecordSetCount** *(integer) --* 

              The number of resource record sets in the hosted zone.

              
            

            - **LinkedService** *(dict) --* 

              If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Amazon Route 53. 

              
              

              - **ServicePrincipal** *(string) --* 

                If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
              

              - **Description** *(string) --* 

                If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
          
        
      
        

        - **Marker** *(string) --* 

          For the second and subsequent calls to ``ListHostedZones`` , ``Marker`` is the value that you specified for the ``marker`` parameter in the request that produced the current response.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag indicating whether there are more hosted zones to be listed. If the response was truncated, you can get more hosted zones by submitting another ``ListHostedZones`` request and specifying the value of ``NextMarker`` in the ``marker`` parameter.

          
        

        - **NextMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , the value of ``NextMarker`` identifies the first hosted zone in the next group of hosted zones. Submit another ``ListHostedZones`` request, and specify the value of ``NextMarker`` from the response in the ``marker`` parameter.

           

          This element is present only if ``IsTruncated`` is ``true`` .

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``maxitems`` parameter in the call to ``ListHostedZones`` that produced the current response.

          
    

  .. py:method:: list_hosted_zones_by_name(**kwargs)

    

    Retrieves a list of your hosted zones in lexicographic order. The response includes a ``HostedZones`` child element for each hosted zone created by the current AWS account. 

     

     ``ListHostedZonesByName`` sorts hosted zones by name with the labels reversed. For example:

     

     ``com.example.www.``  

     

    Note the trailing dot, which can change the sort order in some circumstances.

     

    If the domain name includes escape characters or Punycode, ``ListHostedZonesByName`` alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for exämple.com, you specify ex\344mple.com for the domain name. ``ListHostedZonesByName`` alphabetizes it as:

     

     ``com.ex\344mple.``  

     

    The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see `DNS Domain Name Format <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in the *Amazon Route 53 Developer Guide* .

     

    Amazon Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the ``MaxItems`` parameter to list them in groups of up to 100. The response includes values that help navigate from one group of ``MaxItems`` hosted zones to the next:

     

     
    * The ``DNSName`` and ``HostedZoneId`` elements in the response contain the values, if any, specified for the ``dnsname`` and ``hostedzoneid`` parameters in the request that produced the current response. 
     
    * The ``MaxItems`` element in the response contains the value, if any, that you specified for the ``maxitems`` parameter in the request that produced the current response. 
     
    * If the value of ``IsTruncated`` in the response is true, there are more hosted zones associated with the current AWS account.  If ``IsTruncated`` is false, this response includes the last hosted zone that is associated with the current account. The ``NextDNSName`` element and ``NextHostedZoneId`` elements are omitted from the response. 
     
    * The ``NextDNSName`` and ``NextHostedZoneId`` elements in the response contain the domain name and the hosted zone ID of the next hosted zone that is associated with the current AWS account. If you want to list more hosted zones, make another call to ``ListHostedZonesByName`` , and specify the value of ``NextDNSName`` and ``NextHostedZoneId`` in the ``dnsname`` and ``hostedzoneid`` parameters, respectively. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHostedZonesByName>`_    


    **Request Syntax** 
    ::

      response = client.list_hosted_zones_by_name(
          DNSName='string',
          HostedZoneId='string',
          MaxItems='string'
      )
    :type DNSName: string
    :param DNSName: 

      (Optional) For your first request to ``ListHostedZonesByName`` , include the ``dnsname`` parameter only if you want to specify the name of the first hosted zone in the response. If you don't include the ``dnsname`` parameter, Amazon Route 53 returns all of the hosted zones that were created by the current AWS account, in ASCII order. For subsequent requests, include both ``dnsname`` and ``hostedzoneid`` parameters. For ``dnsname`` , specify the value of ``NextDNSName`` from the previous response.

      

    
    :type HostedZoneId: string
    :param HostedZoneId: 

      (Optional) For your first request to ``ListHostedZonesByName`` , do not include the ``hostedzoneid`` parameter.

       

      If you have more hosted zones than the value of ``maxitems`` , ``ListHostedZonesByName`` returns only the first ``maxitems`` hosted zones. To get the next group of ``maxitems`` hosted zones, submit another request to ``ListHostedZonesByName`` and include both ``dnsname`` and ``hostedzoneid`` parameters. For the value of ``hostedzoneid`` , specify the value of the ``NextHostedZoneId`` element from the previous response.

      

    
    :type MaxItems: string
    :param MaxItems: 

      The maximum number of hosted zones to be included in the response body for this request. If you have more than ``maxitems`` hosted zones, then the value of the ``IsTruncated`` element in the response is true, and the values of ``NextDNSName`` and ``NextHostedZoneId`` specify the first hosted zone in the next group of ``maxitems`` hosted zones. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZones': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'CallerReference': 'string',
                    'Config': {
                        'Comment': 'string',
                        'PrivateZone': True|False
                    },
                    'ResourceRecordSetCount': 123,
                    'LinkedService': {
                        'ServicePrincipal': 'string',
                        'Description': 'string'
                    }
                },
            ],
            'DNSName': 'string',
            'HostedZoneId': 'string',
            'IsTruncated': True|False,
            'NextDNSName': 'string',
            'NextHostedZoneId': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **HostedZones** *(list) --* 

          A complex type that contains general information about the hosted zone.

          
          

          - *(dict) --* 

            A complex type that contains general information about the hosted zone.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the hosted zone when you created it.

              
            

            - **Name** *(string) --* 

              The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

               

              For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see  CreateHostedZone .

              
            

            - **CallerReference** *(string) --* 

              The value that you specified for ``CallerReference`` when you created the hosted zone.

              
            

            - **Config** *(dict) --* 

              A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and ``Comment`` elements don't appear in the response.

              
              

              - **Comment** *(string) --* 

                Any comments that you want to include about the hosted zone.

                
              

              - **PrivateZone** *(boolean) --* 

                A value that indicates whether this is a private hosted zone.

                
          
            

            - **ResourceRecordSetCount** *(integer) --* 

              The number of resource record sets in the hosted zone.

              
            

            - **LinkedService** *(dict) --* 

              If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Amazon Route 53. 

              
              

              - **ServicePrincipal** *(string) --* 

                If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
              

              - **Description** *(string) --* 

                If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
          
        
      
        

        - **DNSName** *(string) --* 

          For the second and subsequent calls to ``ListHostedZonesByName`` , ``DNSName`` is the value that you specified for the ``dnsname`` parameter in the request that produced the current response.

          
        

        - **HostedZoneId** *(string) --* 

          The ID that Amazon Route 53 assigned to the hosted zone when you created it.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more hosted zones to be listed. If the response was truncated, you can get the next group of ``maxitems`` hosted zones by calling ``ListHostedZonesByName`` again and specifying the values of ``NextDNSName`` and ``NextHostedZoneId`` elements in the ``dnsname`` and ``hostedzoneid`` parameters.

          
        

        - **NextDNSName** *(string) --* 

          If ``IsTruncated`` is true, the value of ``NextDNSName`` is the name of the first hosted zone in the next group of ``maxitems`` hosted zones. Call ``ListHostedZonesByName`` again and specify the value of ``NextDNSName`` and ``NextHostedZoneId`` in the ``dnsname`` and ``hostedzoneid`` parameters, respectively.

           

          This element is present only if ``IsTruncated`` is ``true`` .

          
        

        - **NextHostedZoneId** *(string) --* 

          If ``IsTruncated`` is ``true`` , the value of ``NextHostedZoneId`` identifies the first hosted zone in the next group of ``maxitems`` hosted zones. Call ``ListHostedZonesByName`` again and specify the value of ``NextDNSName`` and ``NextHostedZoneId`` in the ``dnsname`` and ``hostedzoneid`` parameters, respectively.

           

          This element is present only if ``IsTruncated`` is ``true`` .

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``maxitems`` parameter in the call to ``ListHostedZonesByName`` that produced the current response.

          
    

  .. py:method:: list_query_logging_configs(**kwargs)

    

    Lists the configurations for DNS query logging that are associated with the current AWS account or the configuration that is associated with a specified hosted zone.

     

    For more information about DNS query logs, see  CreateQueryLoggingConfig . Additional information, including the format of DNS query logs, appears in `Logging DNS Queries <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html>`__ in the *Amazon Route 53 Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListQueryLoggingConfigs>`_    


    **Request Syntax** 
    ::

      response = client.list_query_logging_configs(
          HostedZoneId='string',
          NextToken='string',
          MaxResults='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: 

      (Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in ``HostedZoneId`` . 

       

      If you don't specify a hosted zone ID, ``ListQueryLoggingConfigs`` returns all of the configurations that are associated with the current AWS account.

      

    
    :type NextToken: string
    :param NextToken: 

      (Optional) If the current AWS account has more than ``MaxResults`` query logging configurations, use ``NextToken`` to get the second and subsequent pages of results.

       

      For the first ``ListQueryLoggingConfigs`` request, omit this value.

       

      For the second and subsequent requests, get the value of ``NextToken`` from the previous response and specify that value for ``NextToken`` in the request.

      

    
    :type MaxResults: string
    :param MaxResults: 

      (Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current AWS account has more than ``MaxResults`` configurations, use the value of  ListQueryLoggingConfigsResponse$NextToken in the response to get the next page of results.

       

      If you don't specify a value for ``MaxResults`` , Amazon Route 53 returns up to 100 configurations.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'QueryLoggingConfigs': [
                {
                    'Id': 'string',
                    'HostedZoneId': 'string',
                    'CloudWatchLogsLogGroupArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **QueryLoggingConfigs** *(list) --* 

          An array that contains one  QueryLoggingConfig element for each configuration for DNS query logging that is associated with the current AWS account.

          
          

          - *(dict) --* 

            A complex type that contains information about a configuration for DNS query logging.

            
            

            - **Id** *(string) --* 

              The ID for a configuration for DNS query logging.

              
            

            - **HostedZoneId** *(string) --* 

              The ID of the hosted zone that CloudWatch Logs is logging queries for. 

              
            

            - **CloudWatchLogsLogGroupArn** *(string) --* 

              The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.

              
        
      
        

        - **NextToken** *(string) --* 

          If a response includes the last of the query logging configurations that are associated with the current AWS account, ``NextToken`` doesn't appear in the response.

           

          If a response doesn't include the last of the configurations, you can get more configurations by submitting another  ListQueryLoggingConfigs request. Get the value of ``NextToken`` that Amazon Route 53 returned in the previous response and include it in ``NextToken`` in the next request.

          
    

  .. py:method:: list_resource_record_sets(**kwargs)

    

    Lists the resource record sets in a specified hosted zone.

     

     ``ListResourceRecordSets`` returns up to 100 resource record sets at a time in ASCII order, beginning at a position specified by the ``name`` and ``type`` elements. The action sorts results first by DNS name with the labels reversed, for example:

     

     ``com.example.www.``  

     

    Note the trailing dot, which can change the sort order in some circumstances.

     

    When multiple records have the same DNS name, the action sorts results by the record type.

     

    You can use the name and type elements to adjust the beginning position of the list of resource record sets returned:

      If you do not specify Name or Type  

    The results begin with the first resource record set that the hosted zone contains.

      If you specify Name but not Type  

    The results begin with the first resource record set in the list whose name is greater than or equal to ``Name`` .

      If you specify Type but not Name  

    Amazon Route 53 returns the ``InvalidInput`` error.

      If you specify both Name and Type  

    The results begin with the first resource record set in the list whose name is greater than or equal to ``Name`` , and whose type is greater than or equal to ``Type`` .

       

    This action returns the most current version of the records. This includes records that are ``PENDING`` , and that are not yet available on all Amazon Route 53 DNS servers.

     

    To ensure that you get an accurate listing of the resource record sets for a hosted zone at a point in time, do not submit a ``ChangeResourceRecordSets`` request while you're paging through the results of a ``ListResourceRecordSets`` request. If you do, some pages may display results without the latest changes while other pages display results with the latest changes.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListResourceRecordSets>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_record_sets(
          HostedZoneId='string',
          StartRecordName='string',
          StartRecordType='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
          StartRecordIdentifier='string',
          MaxItems='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone that contains the resource record sets that you want to list.

      

    
    :type StartRecordName: string
    :param StartRecordName: 

      The first name in the lexicographic ordering of resource record sets that you want to list.

      

    
    :type StartRecordType: string
    :param StartRecordType: 

      The type of resource record set to begin the record listing from.

       

      Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``  

       

      Values for weighted, latency, geo, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``  

       

      Values for alias resource record sets: 

       

       
      * **CloudFront distribution** : A or AAAA 
       
      * **Elastic Beanstalk environment that has a regionalized subdomain** : A 
       
      * **ELB load balancer** : A | AAAA 
       
      * **Amazon S3 bucket** : A 
       
      * **Another resource record set in this hosted zone:** The type of the resource record set that the alias references. 
       

       

      Constraint: Specifying ``type`` without specifying ``name`` returns an ``InvalidInput`` error.

      

    
    :type StartRecordIdentifier: string
    :param StartRecordIdentifier: 

       *Weighted resource record sets only:* If results were truncated for a given DNS name and type, specify the value of ``NextRecordIdentifier`` from the previous response to get the next resource record set that has the current DNS name and type.

      

    
    :type MaxItems: string
    :param MaxItems: 

      (Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than ``maxitems`` resource record sets, the value of the ``IsTruncated`` element in the response is ``true`` , and the values of the ``NextRecordName`` and ``NextRecordType`` elements in the response identify the first resource record set in the next group of ``maxitems`` resource record sets.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceRecordSets': [
                {
                    'Name': 'string',
                    'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                    'SetIdentifier': 'string',
                    'Weight': 123,
                    'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                    'GeoLocation': {
                        'ContinentCode': 'string',
                        'CountryCode': 'string',
                        'SubdivisionCode': 'string'
                    },
                    'Failover': 'PRIMARY'|'SECONDARY',
                    'MultiValueAnswer': True|False,
                    'TTL': 123,
                    'ResourceRecords': [
                        {
                            'Value': 'string'
                        },
                    ],
                    'AliasTarget': {
                        'HostedZoneId': 'string',
                        'DNSName': 'string',
                        'EvaluateTargetHealth': True|False
                    },
                    'HealthCheckId': 'string',
                    'TrafficPolicyInstanceId': 'string'
                },
            ],
            'IsTruncated': True|False,
            'NextRecordName': 'string',
            'NextRecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'NextRecordIdentifier': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains list information for the resource record set.

        
        

        - **ResourceRecordSets** *(list) --* 

          Information about multiple resource record sets.

          
          

          - *(dict) --* 

            Information about the resource record set to create or delete.

            
            

            - **Name** *(string) --* 

              The name of the domain you want to perform the action on.

               

              Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical.

               

              For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following:

               

               
              * The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` . 
               
              * The * can't replace any of the middle labels, for example, marketing.*.example.com. 
               
              * If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. 

              .. warning::

                 You can't use the * wildcard for resource records sets that have a type of NS. 

               
               

               

              You can use the * wildcard as the leftmost label in a domain name, for example, ``*.example.com`` . You can't use an * for one of the middle labels, for example, ``marketing.*.example.com`` . In addition, the * must replace the entire label; for example, you can't specify ``prod*.example.com`` .

              
            

            - **Type** *(string) --* 

              The DNS record type. For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``  

               

              Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.

               

              Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``  

               

              .. note::

                 

                SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <http://tools.ietf.org/html/rfc7208#section-14.1>`__ .

                 

               

              Values for alias resource record sets:

               

               
              * **CloudFront distributions:**  ``A``   If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` .  
               
              * **AWS Elastic Beanstalk environment that has a regionalized subdomain** : ``A``   
               
              * **ELB load balancers:**  ``A`` | ``AAAA``   
               
              * **Amazon S3 buckets:**  ``A``   
               
              * **Another resource record set in this hosted zone:** Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` . 
               

              
            

            - **SetIdentifier** *(string) --* 

               *Weighted, Latency, Geo, and Failover resource record sets only:* An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of ``SetIdentifier`` must be unique for each resource record set that has the same combination of DNS name and type. Omit ``SetIdentifier`` for any other types of record sets.

              
            

            - **Weight** *(integer) --* 

               *Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Amazon Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Amazon Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:

               

               
              * You must specify a value for the ``Weight`` element for every weighted resource record set. 
               
              * You can only specify one ``ResourceRecord`` per weighted resource record set. 
               
              * You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets. 
               
              * You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements. 
               
              * For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Amazon Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Amazon Route 53 Active-Active and Active-Passive Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`__ in the *Amazon Route 53 Developer Guide* . 
               

              
            

            - **Region** *(string) --* 

               *Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.

               

              .. note::

                 

                Creating latency and latency alias resource record sets in private hosted zones is not supported.

                 

               

              When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Amazon Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Amazon Route 53 then returns the value that is associated with the selected resource record set.

               

              Note the following:

               

               
              * You can only specify one ``ResourceRecord`` per latency resource record set. 
               
              * You can only create one latency resource record set for each Amazon EC2 Region. 
               
              * You aren't required to create latency resource record sets for all Amazon EC2 Regions. Amazon Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for. 
               
              * You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets. 
               

              
            

            - **GeoLocation** *(dict) --* 

               *Geo location resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` .

               

              .. note::

                 

                Creating geolocation and geolocation alias resource record sets in private hosted zones is not supported.

                 

               

              If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.

               

              You can't create two geolocation resource record sets that specify the same geographic location.

               

              The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements.

               

              .. warning::

                 

                Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Amazon Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` , which handles both queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Amazon Route 53 returns a "no answer" response for queries from those locations.

                 

               

              You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.

              
              

              - **ContinentCode** *(string) --* 

                The two-letter code for the continent.

                 

                Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``  

                 

                Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.

                
              

              - **CountryCode** *(string) --* 

                The two-letter code for the country.

                
              

              - **SubdivisionCode** *(string) --* 

                The code for the subdivision, for example, a state in the United States or a province in Canada.

                
          
            

            - **Failover** *(string) --* 

               *Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets. For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set.

               

              Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets:

               

               
              * When the primary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. 
               
              * When the primary resource record set is unhealthy and the secondary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the secondary resource record set. 
               
              * When the secondary resource record set is unhealthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. 
               
              * If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Amazon Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. 
               

               

              You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets.

               

              For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true.

               

              For more information about configuring failover for Amazon Route 53, see the following topics in the *Amazon Route 53 Developer Guide* : 

               

               
              * `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
               
              * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
               

              
            

            - **MultiValueAnswer** *(boolean) --* 

               *Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` . Note the following:

               

               
              * If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. 
               
              * If you don't associate a health check with a multivalue answer record, Amazon Route 53 always considers the record to be healthy. 
               
              * Amazon Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Amazon Route 53 responds to all DNS queries with all the healthy records. 
               
              * If you have more than eight healthy records, Amazon Route 53 responds to different DNS resolvers with different combinations of healthy records. 
               
              * When all records are unhealthy, Amazon Route 53 responds to DNS queries with up to eight unhealthy records. 
               
              * If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. 
               

               

              You can't create multivalue answer alias records.

              
            

            - **TTL** *(integer) --* 

              The resource record cache time to live (TTL), in seconds. Note the following:

               

               
              * If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target.  
               
              * If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status. 
               
              * All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` . 
               
              * If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` . 
               

              
            

            - **ResourceRecords** *(list) --* 

              Information about the resource records to act upon.

               

              .. note::

                 

                If you're creating an alias resource record set, omit ``ResourceRecords`` .

                 

              
              

              - *(dict) --* 

                Information specific to the resource record.

                 

                .. note::

                   

                  If you're creating an alias resource record set, omit ``ResourceRecord`` .

                   

                
                

                - **Value** *(string) --* 

                  The current or new DNS record value, not to exceed 4,000 characters. In the case of a ``DELETE`` action, if the current value does not match the actual value, an error is returned. For descriptions about how to format ``Value`` for different record types, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .

                   

                  You can specify more than one value for all record types except ``CNAME`` and ``SOA`` . 

                   

                  .. note::

                     

                    If you're creating an alias resource record set, omit ``Value`` .

                     

                  
            
          
            

            - **AliasTarget** *(dict) --* 

               *Alias resource record sets only:* Information about the CloudFront distribution, AWS Elastic Beanstalk environment, ELB load balancer, Amazon S3 bucket, or Amazon Route 53 resource record set to which you're redirecting queries. The AWS Elastic Beanstalk environment must have a regionalized subdomain.

               

              If you're creating resource records sets for a private hosted zone, note the following:

               

               
              * You can't create alias resource record sets for CloudFront distributions in a private hosted zone. 
               
              * Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported. 
               
              * For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__ in the *Amazon Route 53 Developer Guide* . 
               

              
              

              - **HostedZoneId** *(string) --* 

                 *Alias resource records sets only* : The value used depends on where you want to route traffic:

                  CloudFront distribution  

                Specify ``Z2FDTNDATAQYW2`` .

                 

                .. note::

                   

                  Alias resource record sets for CloudFront can't be created in a private zone.

                   

                  Elastic Beanstalk environment  

                Specify the hosted zone ID for the region in which you created the environment. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk <http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region>`__ in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* .

                  ELB load balancer  

                Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:

                 

                 
                * `Elastic Load Balancing <http://docs.aws.amazon.com/general/latest/gr/rande.html#elb_region>`__ table in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers. 
                 
                * **AWS Management Console** : Go to the Amazon EC2 page, choose **Load Balancers** in the navigation pane, select the load balancer, and get the value of the **Hosted zone** field on the **Description** tab. 
                 
                * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                   
                  * Application and Network Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                   

                 
                 
                * **AWS CLI** : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                   
                  * Application and Network Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                   

                 
                 

                  An Amazon S3 bucket configured as a static website  

                Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the `Amazon Simple Storage Service Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ table in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* .

                  Another Amazon Route 53 resource record set in your hosted zone  

                Specify the hosted zone ID of your hosted zone. (An alias resource record set can't reference a resource record set in a different hosted zone.)

                  
              

              - **DNSName** *(string) --* 

                 *Alias resource record sets only:* The value that you specify depends on where you want to route queries:

                  CloudFront distribution  

                Specify the domain name that CloudFront assigned when you created your distribution.

                 

                Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`__ in the *Amazon CloudFront Developer Guide* .

                  Elastic Beanstalk environment  

                Specify the ``CNAME`` attribute for the environment. (The environment must have a regionalized domain name.) You can use the following methods to get the value of the CNAME attribute:

                 

                 
                * *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 
                 
                * *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`__ in the *AWS Elastic Beanstalk API Reference* . 
                 
                * *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <http://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`__ in the *AWS Command Line Interface Reference* . 
                 

                  ELB load balancer  

                Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. 

                 

                 
                * **AWS Management Console** : Go to the EC2 page, choose **Load Balancers** in the navigation pane, choose the load balancer, choose the **Description** tab, and get the value of the **DNS name** field. (If you're routing traffic to a Classic Load Balancer, get the value that begins with **dualstack** .)  
                 
                * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__   
                   
                  * Application and Network Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__   
                   

                 
                 
                * **AWS CLI** : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__   
                   
                  * Application and Network Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__   
                   

                 
                 

                  Amazon S3 bucket that is configured as a static website  

                Specify the domain name of the Amazon S3 website endpoint in which you created the bucket, for example, ``s3-website-us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon Simple Storage Service (S3) Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`__ in the *Amazon Route 53 Developer Guide.*  

                  Another Amazon Route 53 resource record set  

                Specify the value of the ``Name`` element for a resource record set in the current hosted zone.

                  
              

              - **EvaluateTargetHealth** *(boolean) --* 

                 *Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets:* When ``EvaluateTargetHealth`` is ``true`` , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer, or the referenced resource record set.

                 

                Note the following:

                 

                 
                * You can't set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution. 
                 
                * If the AWS resource that you specify in ``AliasTarget`` is a resource record set or a group of resource record sets (for example, a group of weighted resource record sets), but it is not another alias resource record set, we recommend that you associate a health check with all of the resource record sets in the alias target. For more information, see `What Happens When You Omit Health Checks? <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`__ in the *Amazon Route 53 Developer Guide* . 
                 
                * If you specify an Elastic Beanstalk environment in ``HostedZoneId`` and ``DNSName`` , and if the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Amazon Route 53 routes queries to other available resources that are healthy, if any. If the environment contains a single EC2 instance, there are no special requirements. 
                 
                * If you specify an ELB load balancer in ``  AliasTarget `` , ELB routes queries only to the healthy EC2 instances that are registered with the load balancer. If no EC2 instances are healthy or if the load balancer itself is unhealthy, and if ``EvaluateTargetHealth`` is true for the corresponding alias resource record set, Amazon Route 53 routes queries to other resources. When you create a load balancer, you configure settings for ELB health checks; they're not Amazon Route 53 health checks, but they perform a similar function. Do not create Amazon Route 53 health checks for the EC2 instances that you register with an ELB load balancer. For more information, see `How Health Checks Work in More Complex Amazon Route 53 Configurations <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html>`__ in the *Amazon Route 53 Developer Guide* . 
                 
                * We recommend that you set ``EvaluateTargetHealth`` to true only when you have enough idle capacity to handle the failure of one or more endpoints. 
                 

                 

                For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__ in the *Amazon Route 53 Developer Guide* .

                
          
            

            - **HealthCheckId** *(string) --* 

              If you want Amazon Route 53 to return this resource record set in response to a DNS query only when a health check is passing, include the ``HealthCheckId`` element and specify the ID of the applicable health check.

               

              Amazon Route 53 determines whether a resource record set is healthy based on one of the following:

               

               
              * By periodically sending a request to the endpoint that is specified in the health check 
               
              * By aggregating the status of a specified group of health checks (calculated health checks) 
               
              * By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) 
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ .

               

              The ``HealthCheckId`` element is only useful when Amazon Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Amazon Route 53 to base the choice in part on the status of a health check. Configuring health checks only makes sense in the following configurations:

               

               
              * You're checking the health of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets, and you specify health check IDs for all of the resource record sets. If the health check for one resource record set specifies an endpoint that is not healthy, Amazon Route 53 stops responding to queries using the value for that resource record set. 
               
              * You set ``EvaluateTargetHealth`` to true for the resource record sets in a group of alias, weighted alias, latency alias, geolocation alias, or failover alias resource record sets, and you specify health check IDs for all of the resource record sets that are referenced by the alias resource record sets. 
               

               

              .. warning::

                 

                Amazon Route 53 doesn't check the health of the endpoint specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Amazon Route 53 checks the health of the endpoint that you specified in the health check. 

                 

               

              For geolocation resource record sets, if an endpoint is unhealthy, Amazon Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the United States, for North America, and for all locations. If the endpoint for the state resource record set is unhealthy, Amazon Route 53 checks the resource record sets for the United States, for North America, and for all locations (a resource record set for which the value of ``CountryCode`` is ``*`` ), in that order, until it finds a resource record set for which the endpoint is healthy. 

               

              If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets (example.com).

               

              .. warning::

                 

                n this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and then associate the health check with those resource record sets, health check results will be unpredictable.

                 

               

              For more information, see the following topics in the *Amazon Route 53 Developer Guide* :

               

               
              * `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
               
              * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
               

              
            

            - **TrafficPolicyInstanceId** *(string) --* 

              When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. ``TrafficPolicyInstanceId`` is the ID of the traffic policy instance that Amazon Route 53 created this resource record set for.

               

              .. warning::

                 

                To delete the resource record set that is associated with a traffic policy instance, use ``DeleteTrafficPolicyInstance`` . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ``ChangeResourceRecordSets`` , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use. 

                 

              
        
      
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether more resource record sets remain to be listed. If your results were truncated, you can make a follow-up pagination request by using the ``NextRecordName`` element.

          
        

        - **NextRecordName** *(string) --* 

          If the results were truncated, the name of the next record in the list.

           

          This element is present only if ``IsTruncated`` is true. 

          
        

        - **NextRecordType** *(string) --* 

          If the results were truncated, the type of the next record in the list.

           

          This element is present only if ``IsTruncated`` is true. 

          
        

        - **NextRecordIdentifier** *(string) --* 

           *Weighted, latency, geolocation, and failover resource record sets only* : If results were truncated for a given DNS name and type, the value of ``SetIdentifier`` for the next resource record set that has the current DNS name and type.

          
        

        - **MaxItems** *(string) --* 

          The maximum number of records you requested.

          
    

  .. py:method:: list_reusable_delegation_sets(**kwargs)

    

    Retrieves a list of the reusable delegation sets that are associated with the current AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListReusableDelegationSets>`_    


    **Request Syntax** 
    ::

      response = client.list_reusable_delegation_sets(
          Marker='string',
          MaxItems='string'
      )
    :type Marker: string
    :param Marker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more reusable delegation sets. To get another group, submit another ``ListReusableDelegationSets`` request. 

       

      For the value of ``marker`` , specify the value of ``NextMarker`` from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more reusable delegation sets to get.

      

    
    :type MaxItems: string
    :param MaxItems: 

      The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Amazon Route 53 returns only the first 100 reusable delegation sets.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DelegationSets': [
                {
                    'Id': 'string',
                    'CallerReference': 'string',
                    'NameServers': [
                        'string',
                    ]
                },
            ],
            'Marker': 'string',
            'IsTruncated': True|False,
            'NextMarker': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains information about the reusable delegation sets that are associated with the current AWS account.

        
        

        - **DelegationSets** *(list) --* 

          A complex type that contains one ``DelegationSet`` element for each reusable delegation set that was created by the current AWS account.

          
          

          - *(dict) --* 

            A complex type that lists the name servers in a delegation set, as well as the ``CallerReference`` and the ``ID`` for the delegation set.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigns to a reusable delegation set.

              
            

            - **CallerReference** *(string) --* 

              The value that you specified for ``CallerReference`` when you created the reusable delegation set.

              
            

            - **NameServers** *(list) --* 

              A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

              
              

              - *(string) --* 
          
        
      
        

        - **Marker** *(string) --* 

          For the second and subsequent calls to ``ListReusableDelegationSets`` , ``Marker`` is the value that you specified for the ``marker`` parameter in the request that produced the current response.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more reusable delegation sets to be listed.

          
        

        - **NextMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , the value of ``NextMarker`` identifies the next reusable delegation set that Amazon Route 53 will return if you submit another ``ListReusableDelegationSets`` request and specify the value of ``NextMarker`` in the ``marker`` parameter.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``maxitems`` parameter in the call to ``ListReusableDelegationSets`` that produced the current response.

          
    

  .. py:method:: list_tags_for_resource(**kwargs)

    

    Lists tags for one health check or hosted zone. 

     

    For information about using tags for cost allocation, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the *AWS Billing and Cost Management User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_resource(
          ResourceType='healthcheck'|'hostedzone',
          ResourceId='string'
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the resource.

       

       
      * The resource type for health checks is ``healthcheck`` . 
       
      * The resource type for hosted zones is ``hostedzone`` . 
       

      

    
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The ID of the resource for which you want to retrieve tags.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceTagSet': {
                'ResourceType': 'healthcheck'|'hostedzone',
                'ResourceId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains information about the health checks or hosted zones for which you want to list tags.

        
        

        - **ResourceTagSet** *(dict) --* 

          A ``ResourceTagSet`` containing tags associated with the specified resource.

          
          

          - **ResourceType** *(string) --* 

            The type of the resource.

             

             
            * The resource type for health checks is ``healthcheck`` . 
             
            * The resource type for hosted zones is ``hostedzone`` . 
             

            
          

          - **ResourceId** *(string) --* 

            The ID for the specified resource.

            
          

          - **Tags** *(list) --* 

            The tags associated with the specified resource.

            
            

            - *(dict) --* 

              A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

              
              

              - **Key** *(string) --* 

                The value of ``Key`` depends on the operation that you want to perform:

                 

                 
                * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to give the new tag. 
                 
                * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value`` for. 
                 
                * **Delete a key** : ``Key`` is the name of the tag you want to remove. 
                 
                * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon Route 53 console, the list of your health checks includes a **Name** column that lets you see the name that you've given to each health check. 
                 

                
              

              - **Value** *(string) --* 

                The value of ``Value`` depends on the operation that you want to perform:

                 

                 
                * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you want to give the new tag. 
                 
                * **Edit a tag** : ``Value`` is the new value that you want to assign the tag. 
                 

                
          
        
      
    

  .. py:method:: list_tags_for_resources(**kwargs)

    

    Lists tags for up to 10 health checks or hosted zones.

     

    For information about using tags for cost allocation, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the *AWS Billing and Cost Management User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTagsForResources>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_resources(
          ResourceType='healthcheck'|'hostedzone',
          ResourceIds=[
              'string',
          ]
      )
    :type ResourceType: string
    :param ResourceType: **[REQUIRED]** 

      The type of the resources.

       

       
      * The resource type for health checks is ``healthcheck`` . 
       
      * The resource type for hosted zones is ``hostedzone`` . 
       

      

    
    :type ResourceIds: list
    :param ResourceIds: **[REQUIRED]** 

      A complex type that contains the ResourceId element for each resource for which you want to get a list of tags.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceTagSets': [
                {
                    'ResourceType': 'healthcheck'|'hostedzone',
                    'ResourceId': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type containing tags for the specified resources.

        
        

        - **ResourceTagSets** *(list) --* 

          A list of ``ResourceTagSet`` s containing tags associated with the specified resources.

          
          

          - *(dict) --* 

            A complex type containing a resource and its associated tags.

            
            

            - **ResourceType** *(string) --* 

              The type of the resource.

               

               
              * The resource type for health checks is ``healthcheck`` . 
               
              * The resource type for hosted zones is ``hostedzone`` . 
               

              
            

            - **ResourceId** *(string) --* 

              The ID for the specified resource.

              
            

            - **Tags** *(list) --* 

              The tags associated with the specified resource.

              
              

              - *(dict) --* 

                A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

                
                

                - **Key** *(string) --* 

                  The value of ``Key`` depends on the operation that you want to perform:

                   

                   
                  * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to give the new tag. 
                   
                  * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value`` for. 
                   
                  * **Delete a key** : ``Key`` is the name of the tag you want to remove. 
                   
                  * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon Route 53 console, the list of your health checks includes a **Name** column that lets you see the name that you've given to each health check. 
                   

                  
                

                - **Value** *(string) --* 

                  The value of ``Value`` depends on the operation that you want to perform:

                   

                   
                  * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you want to give the new tag. 
                   
                  * **Edit a tag** : ``Value`` is the new value that you want to assign the tag. 
                   

                  
            
          
        
      
    

  .. py:method:: list_traffic_policies(**kwargs)

    

    Gets information about the latest version for every traffic policy that is associated with the current AWS account. Policies are listed in the order in which they were created. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTrafficPolicies>`_    


    **Request Syntax** 
    ::

      response = client.list_traffic_policies(
          TrafficPolicyIdMarker='string',
          MaxItems='string'
      )
    :type TrafficPolicyIdMarker: string
    :param TrafficPolicyIdMarker: 

      (Conditional) For your first request to ``ListTrafficPolicies`` , don't include the ``TrafficPolicyIdMarker`` parameter.

       

      If you have more traffic policies than the value of ``MaxItems`` , ``ListTrafficPolicies`` returns only the first ``MaxItems`` traffic policies. To get the next group of policies, submit another request to ``ListTrafficPolicies`` . For the value of ``TrafficPolicyIdMarker`` , specify the value of ``TrafficPolicyIdMarker`` that was returned in the previous response.

      

    
    :type MaxItems: string
    :param MaxItems: 

      (Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than ``MaxItems`` traffic policies, the value of ``IsTruncated`` in the response is ``true`` , and the value of ``TrafficPolicyIdMarker`` is the ID of the first traffic policy that Amazon Route 53 will return if you submit another request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicySummaries': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                    'LatestVersion': 123,
                    'TrafficPolicyCount': 123
                },
            ],
            'IsTruncated': True|False,
            'TrafficPolicyIdMarker': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **TrafficPolicySummaries** *(list) --* 

          A list that contains one ``TrafficPolicySummary`` element for each traffic policy that was created by the current AWS account.

          
          

          - *(dict) --* 

            A complex type that contains information about the latest version of one traffic policy that is associated with the current AWS account.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the traffic policy when you created it.

              
            

            - **Name** *(string) --* 

              The name that you specified for the traffic policy when you created it.

              
            

            - **Type** *(string) --* 

              The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

              
            

            - **LatestVersion** *(integer) --* 

              The version number of the latest version of the traffic policy.

              
            

            - **TrafficPolicyCount** *(integer) --* 

              The number of traffic policies that are associated with the current AWS account.

              
        
      
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another ``ListTrafficPolicies`` request and specifying the value of ``TrafficPolicyIdMarker`` in the ``TrafficPolicyIdMarker`` request parameter.

          
        

        - **TrafficPolicyIdMarker** *(string) --* 

          If the value of ``IsTruncated`` is ``true`` , ``TrafficPolicyIdMarker`` is the ID of the first traffic policy in the next group of ``MaxItems`` traffic policies.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``MaxItems`` parameter in the ``ListTrafficPolicies`` request that produced the current response.

          
    

  .. py:method:: list_traffic_policy_instances(**kwargs)

    

    Gets information about the traffic policy instances that you created by using the current AWS account.

     

    .. note::

       

      After you submit an ``UpdateTrafficPolicyInstance`` request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the ``State`` response element.

       

     

    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the ``MaxItems`` parameter to list them in groups of up to 100.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTrafficPolicyInstances>`_    


    **Request Syntax** 
    ::

      response = client.list_traffic_policy_instances(
          HostedZoneIdMarker='string',
          TrafficPolicyInstanceNameMarker='string',
          TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
          MaxItems='string'
      )
    :type HostedZoneIdMarker: string
    :param HostedZoneIdMarker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstances`` request. For the value of ``HostedZoneId`` , specify the value of ``HostedZoneIdMarker`` from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of traffic policy instances.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstances`` request. For the value of ``trafficpolicyinstancename`` , specify the value of ``TrafficPolicyInstanceNameMarker`` from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstances`` request. For the value of ``trafficpolicyinstancetype`` , specify the value of ``TrafficPolicyInstanceTypeMarker`` from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type MaxItems: string
    :param MaxItems: 

      The maximum number of traffic policy instances that you want Amazon Route 53 to return in response to a ``ListTrafficPolicyInstances`` request. If you have more than ``MaxItems`` traffic policy instances, the value of the ``IsTruncated`` element in the response is ``true`` , and the values of ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and ``TrafficPolicyInstanceTypeMarker`` represent the first traffic policy instance in the next group of ``MaxItems`` traffic policy instances.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicyInstances': [
                {
                    'Id': 'string',
                    'HostedZoneId': 'string',
                    'Name': 'string',
                    'TTL': 123,
                    'State': 'string',
                    'Message': 'string',
                    'TrafficPolicyId': 'string',
                    'TrafficPolicyVersion': 123,
                    'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
                },
            ],
            'HostedZoneIdMarker': 'string',
            'TrafficPolicyInstanceNameMarker': 'string',
            'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'IsTruncated': True|False,
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **TrafficPolicyInstances** *(list) --* 

          A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance that matches the elements in the request.

          
          

          - *(dict) --* 

            A complex type that contains settings for the new traffic policy instance.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the new traffic policy instance.

              
            

            - **HostedZoneId** *(string) --* 

              The ID of the hosted zone that Amazon Route 53 created resource record sets in.

              
            

            - **Name** *(string) --* 

              The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance. 

              
            

            - **TTL** *(integer) --* 

              The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

              
            

            - **State** *(string) --* 

              The value of ``State`` is one of the following values:

                Applied  

              Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Amazon Route 53 edge locations.

                Creating  

              Amazon Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

                Failed  

              Amazon Route 53 wasn't able to create or update the resource record sets. When the value of ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to fail.

                
            

            - **Message** *(string) --* 

              If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is another value, ``Message`` is empty.

              
            

            - **TrafficPolicyId** *(string) --* 

              The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

              
            

            - **TrafficPolicyVersion** *(integer) --* 

              The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

              
            

            - **TrafficPolicyType** *(string) --* 

              The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance. 

              
        
      
        

        - **HostedZoneIdMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , ``HostedZoneIdMarker`` is the ID of the hosted zone of the first traffic policy instance that Amazon Route 53 will return if you submit another ``ListTrafficPolicyInstances`` request. 

          
        

        - **TrafficPolicyInstanceNameMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceNameMarker`` is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another ``ListTrafficPolicyInstances`` request. 

          
        

        - **TrafficPolicyInstanceTypeMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceTypeMarker`` is the DNS type of the resource record sets that are associated with the first traffic policy instance that Amazon Route 53 will return if you submit another ``ListTrafficPolicyInstances`` request. 

          
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get more traffic policy instances by calling ``ListTrafficPolicyInstances`` again and specifying the values of the ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and ``TrafficPolicyInstanceTypeMarker`` in the corresponding request parameters.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``MaxItems`` parameter in the call to ``ListTrafficPolicyInstances`` that produced the current response.

          
    

  .. py:method:: list_traffic_policy_instances_by_hosted_zone(**kwargs)

    

    Gets information about the traffic policy instances that you created in a specified hosted zone.

     

    .. note::

       

      After you submit a ``CreateTrafficPolicyInstance`` or an ``UpdateTrafficPolicyInstance`` request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the ``State`` response element.

       

     

    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the ``MaxItems`` parameter to list them in groups of up to 100.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTrafficPolicyInstancesByHostedZone>`_    


    **Request Syntax** 
    ::

      response = client.list_traffic_policy_instances_by_hosted_zone(
          HostedZoneId='string',
          TrafficPolicyInstanceNameMarker='string',
          TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
          MaxItems='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone that you want to list traffic policy instances for.

      

    
    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: 

      If the value of ``IsTruncated`` in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstances`` request. For the value of ``trafficpolicyinstancename`` , specify the value of ``TrafficPolicyInstanceNameMarker`` from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: 

      If the value of ``IsTruncated`` in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstances`` request. For the value of ``trafficpolicyinstancetype`` , specify the value of ``TrafficPolicyInstanceTypeMarker`` from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type MaxItems: string
    :param MaxItems: 

      The maximum number of traffic policy instances to be included in the response body for this request. If you have more than ``MaxItems`` traffic policy instances, the value of the ``IsTruncated`` element in the response is ``true`` , and the values of ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and ``TrafficPolicyInstanceTypeMarker`` represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicyInstances': [
                {
                    'Id': 'string',
                    'HostedZoneId': 'string',
                    'Name': 'string',
                    'TTL': 123,
                    'State': 'string',
                    'Message': 'string',
                    'TrafficPolicyId': 'string',
                    'TrafficPolicyVersion': 123,
                    'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
                },
            ],
            'TrafficPolicyInstanceNameMarker': 'string',
            'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'IsTruncated': True|False,
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **TrafficPolicyInstances** *(list) --* 

          A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance that matches the elements in the request. 

          
          

          - *(dict) --* 

            A complex type that contains settings for the new traffic policy instance.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the new traffic policy instance.

              
            

            - **HostedZoneId** *(string) --* 

              The ID of the hosted zone that Amazon Route 53 created resource record sets in.

              
            

            - **Name** *(string) --* 

              The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance. 

              
            

            - **TTL** *(integer) --* 

              The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

              
            

            - **State** *(string) --* 

              The value of ``State`` is one of the following values:

                Applied  

              Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Amazon Route 53 edge locations.

                Creating  

              Amazon Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

                Failed  

              Amazon Route 53 wasn't able to create or update the resource record sets. When the value of ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to fail.

                
            

            - **Message** *(string) --* 

              If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is another value, ``Message`` is empty.

              
            

            - **TrafficPolicyId** *(string) --* 

              The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

              
            

            - **TrafficPolicyVersion** *(integer) --* 

              The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

              
            

            - **TrafficPolicyType** *(string) --* 

              The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance. 

              
        
      
        

        - **TrafficPolicyInstanceNameMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceNameMarker`` is the name of the first traffic policy instance in the next group of traffic policy instances.

          
        

        - **TrafficPolicyInstanceTypeMarker** *(string) --* 

          If ``IsTruncated`` is true, ``TrafficPolicyInstanceTypeMarker`` is the DNS type of the resource record sets that are associated with the first traffic policy instance in the next group of traffic policy instances.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get the next group of traffic policy instances by submitting another ``ListTrafficPolicyInstancesByHostedZone`` request and specifying the values of ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and ``TrafficPolicyInstanceTypeMarker`` in the corresponding request parameters.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``MaxItems`` parameter in the ``ListTrafficPolicyInstancesByHostedZone`` request that produced the current response.

          
    

  .. py:method:: list_traffic_policy_instances_by_policy(**kwargs)

    

    Gets information about the traffic policy instances that you created by using a specify traffic policy version.

     

    .. note::

       

      After you submit a ``CreateTrafficPolicyInstance`` or an ``UpdateTrafficPolicyInstance`` request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the ``State`` response element.

       

     

    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the ``MaxItems`` parameter to list them in groups of up to 100.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTrafficPolicyInstancesByPolicy>`_    


    **Request Syntax** 
    ::

      response = client.list_traffic_policy_instances_by_policy(
          TrafficPolicyId='string',
          TrafficPolicyVersion=123,
          HostedZoneIdMarker='string',
          TrafficPolicyInstanceNameMarker='string',
          TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
          MaxItems='string'
      )
    :type TrafficPolicyId: string
    :param TrafficPolicyId: **[REQUIRED]** 

      The ID of the traffic policy for which you want to list traffic policy instances.

      

    
    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: **[REQUIRED]** 

      The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by ``TrafficPolicyId`` .

      

    
    :type HostedZoneIdMarker: string
    :param HostedZoneIdMarker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstancesByPolicy`` request. 

       

      For the value of ``hostedzoneid`` , specify the value of ``HostedZoneIdMarker`` from the previous response, which is the hosted zone ID of the first traffic policy instance that Amazon Route 53 will return if you submit another request.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstancesByPolicy`` request.

       

      For the value of ``trafficpolicyinstancename`` , specify the value of ``TrafficPolicyInstanceNameMarker`` from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: 

      If the value of ``IsTruncated`` in the previous response was ``true`` , you have more traffic policy instances. To get more traffic policy instances, submit another ``ListTrafficPolicyInstancesByPolicy`` request.

       

      For the value of ``trafficpolicyinstancetype`` , specify the value of ``TrafficPolicyInstanceTypeMarker`` from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.

       

      If the value of ``IsTruncated`` in the previous response was ``false`` , there are no more traffic policy instances to get.

      

    
    :type MaxItems: string
    :param MaxItems: 

      The maximum number of traffic policy instances to be included in the response body for this request. If you have more than ``MaxItems`` traffic policy instances, the value of the ``IsTruncated`` element in the response is ``true`` , and the values of ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and ``TrafficPolicyInstanceTypeMarker`` represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicyInstances': [
                {
                    'Id': 'string',
                    'HostedZoneId': 'string',
                    'Name': 'string',
                    'TTL': 123,
                    'State': 'string',
                    'Message': 'string',
                    'TrafficPolicyId': 'string',
                    'TrafficPolicyVersion': 123,
                    'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
                },
            ],
            'HostedZoneIdMarker': 'string',
            'TrafficPolicyInstanceNameMarker': 'string',
            'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'IsTruncated': True|False,
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **TrafficPolicyInstances** *(list) --* 

          A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance that matches the elements in the request.

          
          

          - *(dict) --* 

            A complex type that contains settings for the new traffic policy instance.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the new traffic policy instance.

              
            

            - **HostedZoneId** *(string) --* 

              The ID of the hosted zone that Amazon Route 53 created resource record sets in.

              
            

            - **Name** *(string) --* 

              The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance. 

              
            

            - **TTL** *(integer) --* 

              The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

              
            

            - **State** *(string) --* 

              The value of ``State`` is one of the following values:

                Applied  

              Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Amazon Route 53 edge locations.

                Creating  

              Amazon Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

                Failed  

              Amazon Route 53 wasn't able to create or update the resource record sets. When the value of ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to fail.

                
            

            - **Message** *(string) --* 

              If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is another value, ``Message`` is empty.

              
            

            - **TrafficPolicyId** *(string) --* 

              The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

              
            

            - **TrafficPolicyVersion** *(integer) --* 

              The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

              
            

            - **TrafficPolicyType** *(string) --* 

              The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance. 

              
        
      
        

        - **HostedZoneIdMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , ``HostedZoneIdMarker`` is the ID of the hosted zone of the first traffic policy instance in the next group of traffic policy instances.

          
        

        - **TrafficPolicyInstanceNameMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceNameMarker`` is the name of the first traffic policy instance in the next group of ``MaxItems`` traffic policy instances.

          
        

        - **TrafficPolicyInstanceTypeMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceTypeMarker`` is the DNS type of the resource record sets that are associated with the first traffic policy instance in the next group of ``MaxItems`` traffic policy instances.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get the next group of traffic policy instances by calling ``ListTrafficPolicyInstancesByPolicy`` again and specifying the values of the ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and ``TrafficPolicyInstanceTypeMarker`` elements in the corresponding request parameters.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``MaxItems`` parameter in the call to ``ListTrafficPolicyInstancesByPolicy`` that produced the current response.

          
    

  .. py:method:: list_traffic_policy_versions(**kwargs)

    

    Gets information about all of the versions for a specified traffic policy.

     

    Traffic policy versions are listed in numerical order by ``VersionNumber`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTrafficPolicyVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_traffic_policy_versions(
          Id='string',
          TrafficPolicyVersionMarker='string',
          MaxItems='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      Specify the value of ``Id`` of the traffic policy for which you want to list all versions.

      

    
    :type TrafficPolicyVersionMarker: string
    :param TrafficPolicyVersionMarker: 

      For your first request to ``ListTrafficPolicyVersions`` , don't include the ``TrafficPolicyVersionMarker`` parameter.

       

      If you have more traffic policy versions than the value of ``MaxItems`` , ``ListTrafficPolicyVersions`` returns only the first group of ``MaxItems`` versions. To get more traffic policy versions, submit another ``ListTrafficPolicyVersions`` request. For the value of ``TrafficPolicyVersionMarker`` , specify the value of ``TrafficPolicyVersionMarker`` in the previous response.

      

    
    :type MaxItems: string
    :param MaxItems: 

      The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than ``MaxItems`` versions, the value of ``IsTruncated`` in the response is ``true`` , and the value of the ``TrafficPolicyVersionMarker`` element is the ID of the first version that Amazon Route 53 will return if you submit another request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicies': [
                {
                    'Id': 'string',
                    'Version': 123,
                    'Name': 'string',
                    'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                    'Document': 'string',
                    'Comment': 'string'
                },
            ],
            'IsTruncated': True|False,
            'TrafficPolicyVersionMarker': 'string',
            'MaxItems': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **TrafficPolicies** *(list) --* 

          A list that contains one ``TrafficPolicy`` element for each traffic policy version that is associated with the specified traffic policy.

          
          

          - *(dict) --* 

            A complex type that contains settings for a traffic policy.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to a traffic policy when you created it.

              
            

            - **Version** *(integer) --* 

              The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of ``Version`` is always 1.

              
            

            - **Name** *(string) --* 

              The name that you specified when you created the traffic policy.

              
            

            - **Type** *(string) --* 

              The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

              
            

            - **Document** *(string) --* 

              The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the JSON format, see `Traffic Policy Document Format <http://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__ .

              
            

            - **Comment** *(string) --* 

              The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

              
        
      
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another ``ListTrafficPolicyVersions`` request and specifying the value of ``NextMarker`` in the ``marker`` parameter.

          
        

        - **TrafficPolicyVersionMarker** *(string) --* 

          If ``IsTruncated`` is ``true`` , the value of ``TrafficPolicyVersionMarker`` identifies the first traffic policy that Amazon Route 53 will return if you submit another request. Call ``ListTrafficPolicyVersions`` again and specify the value of ``TrafficPolicyVersionMarker`` in the ``TrafficPolicyVersionMarker`` request parameter.

           

          This element is present only if ``IsTruncated`` is ``true`` .

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``maxitems`` parameter in the ``ListTrafficPolicyVersions`` request that produced the current response.

          
    

  .. py:method:: list_vpc_association_authorizations(**kwargs)

    

    Gets a list of the VPCs that were created by other accounts and that can be associated with a specified hosted zone because you've submitted one or more ``CreateVPCAssociationAuthorization`` requests. 

     

    The response includes a ``VPCs`` element with a ``VPC`` child element for each VPC that can be associated with the hosted zone.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListVPCAssociationAuthorizations>`_    


    **Request Syntax** 
    ::

      response = client.list_vpc_association_authorizations(
          HostedZoneId='string',
          NextToken='string',
          MaxResults='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.

      

    
    :type NextToken: string
    :param NextToken: 

       *Optional* : If a response includes a ``NextToken`` element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of ``NextToken`` from the response in the ``nexttoken`` parameter in another ``ListVPCAssociationAuthorizations`` request.

      

    
    :type MaxResults: string
    :param MaxResults: 

       *Optional* : An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don't specify a value for ``MaxResults`` , Amazon Route 53 returns up to 50 VPCs per page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZoneId': 'string',
            'NextToken': 'string',
            'VPCs': [
                {
                    'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'ca-central-1'|'cn-north-1',
                    'VPCId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the request.

        
        

        - **HostedZoneId** *(string) --* 

          The ID of the hosted zone that you can associate the listed VPCs with.

          
        

        - **NextToken** *(string) --* 

          When the response includes a ``NextToken`` element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of VPCs, submit another ``ListVPCAssociationAuthorizations`` request, and include the value of the ``NextToken`` element from the response in the ``nexttoken`` request parameter.

          
        

        - **VPCs** *(list) --* 

          The list of VPCs that are authorized to be associated with the specified hosted zone.

          
          

          - *(dict) --* 

            (Private hosted zones only) A complex type that contains information about an Amazon VPC.

            
            

            - **VPCRegion** *(string) --* 

              (Private hosted zones only) The region in which you created an Amazon VPC.

              
            

            - **VPCId** *(string) --* 

              (Private hosted zones only) The ID of an Amazon VPC. 

              
        
      
    

  .. py:method:: test_dns_answer(**kwargs)

    

    Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/TestDNSAnswer>`_    


    **Request Syntax** 
    ::

      response = client.test_dns_answer(
          HostedZoneId='string',
          RecordName='string',
          RecordType='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
          ResolverIP='string',
          EDNS0ClientSubnetIP='string',
          EDNS0ClientSubnetMask='string'
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.

      

    
    :type RecordName: string
    :param RecordName: **[REQUIRED]** 

      The name of the resource record set that you want Amazon Route 53 to simulate a query for.

      

    
    :type RecordType: string
    :param RecordType: **[REQUIRED]** 

      The type of the resource record set.

      

    
    :type ResolverIP: string
    :param ResolverIP: 

      If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, ``TestDnsAnswer`` uses the IP address of a DNS resolver in the AWS US East (N. Virginia) Region (``us-east-1`` ).

      

    
    :type EDNS0ClientSubnetIP: string
    :param EDNS0ClientSubnetIP: 

      If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, ``192.0.2.44`` or ``2001:db8:85a3::8a2e:370:7334`` .

      

    
    :type EDNS0ClientSubnetMask: string
    :param EDNS0ClientSubnetMask: 

      If you specify an IP address for ``edns0clientsubnetip`` , you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify ``192.0.2.44`` for ``edns0clientsubnetip`` and ``24`` for ``edns0clientsubnetmask`` , the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Nameserver': 'string',
            'RecordName': 'string',
            'RecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'RecordData': [
                'string',
            ],
            'ResponseCode': 'string',
            'Protocol': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``TestDNSAnswer`` request. 

        
        

        - **Nameserver** *(string) --* 

          The Amazon Route 53 name server used to respond to the request.

          
        

        - **RecordName** *(string) --* 

          The name of the resource record set that you submitted a request for.

          
        

        - **RecordType** *(string) --* 

          The type of the resource record set that you submitted a request for.

          
        

        - **RecordData** *(list) --* 

          A list that contains values that Amazon Route 53 returned for this resource record set.

          
          

          - *(string) --* 

            A value that Amazon Route 53 returned for this resource record set. A ``RecordDataEntry`` element is one of the following:

             

             
            * For non-alias resource record sets, a ``RecordDataEntry`` element contains one value in the resource record set. If the resource record set contains multiple values, the response includes one ``RecordDataEntry`` element for each value. 
             
            * For multiple resource record sets that have the same name and type, which includes weighted, latency, geolocation, and failover, a ``RecordDataEntry`` element contains the value from the appropriate resource record set based on the request. 
             
            * For alias resource record sets that refer to AWS resources other than another resource record set, the ``RecordDataEntry`` element contains an IP address or a domain name for the AWS resource, depending on the type of resource. 
             
            * For alias resource record sets that refer to other resource record sets, a ``RecordDataEntry`` element contains one value from the referenced resource record set. If the referenced resource record set contains multiple values, the response includes one ``RecordDataEntry`` element for each value. 
             

            
      
        

        - **ResponseCode** *(string) --* 

          A code that indicates whether the request is valid or not. The most common response code is ``NOERROR`` , meaning that the request is valid. If the response is not valid, Amazon Route 53 returns a response code that describes the error. For a list of possible response codes, see `DNS RCODES <http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6>`__ on the IANA website. 

          
        

        - **Protocol** *(string) --* 

          The protocol that Amazon Route 53 used to respond to the request, either ``UDP`` or ``TCP`` . 

          
    

  .. py:method:: update_health_check(**kwargs)

    

    Updates an existing health check. Note that some values can't be updated. 

     

    For more information about updating health checks, see `Creating, Updating, and Deleting Health Checks <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html>`__ in the *Amazon Route 53 Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/UpdateHealthCheck>`_    


    **Request Syntax** 
    ::

      response = client.update_health_check(
          HealthCheckId='string',
          HealthCheckVersion=123,
          IPAddress='string',
          Port=123,
          ResourcePath='string',
          FullyQualifiedDomainName='string',
          SearchString='string',
          FailureThreshold=123,
          Inverted=True|False,
          HealthThreshold=123,
          ChildHealthChecks=[
              'string',
          ],
          EnableSNI=True|False,
          Regions=[
              'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
          ],
          AlarmIdentifier={
              'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
              'Name': 'string'
          },
          InsufficientDataHealthStatus='Healthy'|'Unhealthy'|'LastKnownStatus',
          ResetElements=[
              'FullyQualifiedDomainName'|'Regions'|'ResourcePath'|'ChildHealthChecks',
          ]
      )
    :type HealthCheckId: string
    :param HealthCheckId: **[REQUIRED]** 

      The ID for the health check for which you want detailed information. When you created the health check, ``CreateHealthCheck`` returned the ID in the response, in the ``HealthCheckId`` element.

      

    
    :type HealthCheckVersion: integer
    :param HealthCheckVersion: 

      A sequential counter that Amazon Route 53 sets to ``1`` when you create a health check and increments by 1 each time you update settings for the health check.

       

      We recommend that you use ``GetHealthCheck`` or ``ListHealthChecks`` to get the current value of ``HealthCheckVersion`` for the health check that you want to update, and that you include that value in your ``UpdateHealthCheck`` request. This prevents Amazon Route 53 from overwriting an intervening update:

       

       
      * If the value in the ``UpdateHealthCheck`` request matches the value of ``HealthCheckVersion`` in the health check, Amazon Route 53 updates the health check with the new settings. 
       
      * If the value of ``HealthCheckVersion`` in the health check is greater, the health check was changed after you got the version number. Amazon Route 53 does not update the health check, and it returns a ``HealthCheckVersionMismatch`` error. 
       

      

    
    :type IPAddress: string
    :param IPAddress: 

      The IPv4 or IPv6 IP address for the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address that is returned by DNS, Amazon Route 53 then checks the health of the endpoint.

       

      Use one of the following formats for the value of ``IPAddress`` : 

       

       
      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
       
      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
       

       

      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance never changes. For more information, see the applicable documentation:

       

       
      * Linux: `Elastic IP Addresses (EIP) <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ in the *Amazon EC2 User Guide for Linux Instances*   
       
      * Windows: `Elastic IP Addresses (EIP) <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.html>`__ in the *Amazon EC2 User Guide for Windows Instances*   
       

       

      .. note::

         

        If a health check already has a value for ``IPAddress`` , you can change the value. However, you can't update an existing health check to add or remove the value of ``IPAddress`` . 

         

       

      For more information, see  UpdateHealthCheckRequest$FullyQualifiedDomainName .

       

      Constraints: Amazon Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

       

       
      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
       
      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
       
      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
       

      

    
    :type Port: integer
    :param Port: 

      The port on the endpoint on which you want Amazon Route 53 to perform health checks.

      

    
    :type ResourcePath: string
    :param ResourcePath: 

      The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html. 

       

      Specify this value only if you want to change it.

      

    
    :type FullyQualifiedDomainName: string
    :param FullyQualifiedDomainName: 

      Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

       

      .. note::

         

        If a health check already has a value for ``IPAddress`` , you can change the value. However, you can't update an existing health check to add or remove the value of ``IPAddress`` . 

         

       

       **If you specify a value for**  ``IPAddress`` :

       

      Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks.

       

      When Amazon Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

       

       
      * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
       
      * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
       
      * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Amazon Route 53 passes * ``FullyQualifiedDomainName`` :``Port`` * to the endpoint in the ``Host`` header. 
       

       

      If you don't specify a value for ``FullyQualifiedDomainName`` , Amazon Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the above cases.

       

       **If you don't specify a value for**  ``IPAddress`` :

       

      If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to the domain that you specify in ``FullyQualifiedDomainName`` at the interval you specify in ``RequestInterval`` . Using an IPv4 address that is returned by DNS, Amazon Route 53 then checks the health of the endpoint.

       

      .. note::

         

        If you don't specify a value for ``IPAddress`` , Amazon Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

         

       

      If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets (www.example.com).

       

      .. warning::

         

        In this configuration, if the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

         

       

      In addition, if the value of ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Amazon Route 53 doesn't pass a ``Host`` header.

      

    
    :type SearchString: string
    :param SearchString: 

      If the value of ``Type`` is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy. (You can't change the value of ``Type`` when you update a health check.)

      

    
    :type FailureThreshold: integer
    :param FailureThreshold: 

      The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

       

      If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

      

    
    :type Inverted: boolean
    :param Inverted: 

      Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

      

    
    :type HealthThreshold: integer
    :param HealthThreshold: 

      The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the ``ChildHealthChecks`` and ``ChildHealthCheck`` elements.

       

      Note the following:

       

       
      * If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy. 
       
      * If you specify ``0`` , Amazon Route 53 always considers this health check to be healthy. 
       

      

    
    :type ChildHealthChecks: list
    :param ChildHealthChecks: 

      A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

      

    
      - *(string) --* 

      
  
    :type EnableSNI: boolean
    :param EnableSNI: 

      Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during ``TLS`` negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

       

      Some endpoints require that HTTPS requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be SSL alert ``handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

       

      The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

      

    
    :type Regions: list
    :param Regions: 

      A complex type that contains one ``Region`` element for each region that you want Amazon Route 53 health checkers to check the specified endpoint from.

      

    
      - *(string) --* 

      
  
    :type AlarmIdentifier: dict
    :param AlarmIdentifier: 

      A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

      

    
      - **Region** *(string) --* **[REQUIRED]** 

        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

         

        For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

        

      
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

        

      
    
    :type InsufficientDataHealthStatus: string
    :param InsufficientDataHealthStatus: 

      When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

       

       
      * ``Healthy`` : Amazon Route 53 considers the health check to be healthy. 
       
      * ``Unhealthy`` : Amazon Route 53 considers the health check to be unhealthy. 
       
      * ``LastKnownStatus`` : Amazon Route 53 uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
       

      

    
    :type ResetElements: list
    :param ResetElements: 

      A complex type that contains one ``ResettableElementName`` element for each element that you want to reset to the default value. Valid values for ``ResettableElementName`` include the following:

       

       
      * ``ChildHealthChecks`` : Amazon Route 53 resets  HealthCheckConfig$ChildHealthChecks to null. 
       
      * ``FullyQualifiedDomainName`` : Amazon Route 53 resets  HealthCheckConfig$FullyQualifiedDomainName to null. 
       
      * ``Regions`` : Amazon Route 53 resets the  HealthCheckConfig$Regions list to the default set of regions.  
       
      * ``ResourcePath`` : Amazon Route 53 resets  HealthCheckConfig$ResourcePath to null. 
       

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthCheck': {
                'Id': 'string',
                'CallerReference': 'string',
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                },
                'HealthCheckConfig': {
                    'IPAddress': 'string',
                    'Port': 123,
                    'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                    'ResourcePath': 'string',
                    'FullyQualifiedDomainName': 'string',
                    'SearchString': 'string',
                    'RequestInterval': 123,
                    'FailureThreshold': 123,
                    'MeasureLatency': True|False,
                    'Inverted': True|False,
                    'HealthThreshold': 123,
                    'ChildHealthChecks': [
                        'string',
                    ],
                    'EnableSNI': True|False,
                    'Regions': [
                        'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                    ],
                    'AlarmIdentifier': {
                        'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                        'Name': 'string'
                    },
                    'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
                },
                'HealthCheckVersion': 123,
                'CloudWatchAlarmConfiguration': {
                    'EvaluationPeriods': 123,
                    'Threshold': 123.0,
                    'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                    'Period': 123,
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **HealthCheck** *(dict) --* 

          A complex type that contains information about one health check that is associated with the current AWS account.

          
          

          - **Id** *(string) --* 

            The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. 

            
          

          - **CallerReference** *(string) --* 

            A unique string that you specified when you created the health check.

            
          

          - **LinkedService** *(dict) --* 

            If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can't edit or delete it using Amazon Route 53. 

            
            

            - **ServicePrincipal** *(string) --* 

              If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
            

            - **Description** *(string) --* 

              If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
        
          

          - **HealthCheckConfig** *(dict) --* 

            A complex type that contains detailed information about one health check.

            
            

            - **IPAddress** *(string) --* 

              The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Amazon Route 53 then checks the health of the endpoint.

               

              Use one of the following formats for the value of ``IPAddress`` : 

               

               
              * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
               
              * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
               

               

              If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.

               

              For more information, see  HealthCheckConfig$FullyQualifiedDomainName .

               

              Constraints: Amazon Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

               

               
              * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
               
              * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
               
              * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
               

               

              When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

              
            

            - **Port** *(integer) --* 

              The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

              
            

            - **Type** *(string) --* 

              The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

               

              .. warning::

                 

                You can't change the value of ``Type`` after you create a health check.

                 

               

              You can create the following types of health checks:

               

               
              * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
               
              * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

              .. warning::

                 If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

               
               
              * **HTTP_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
               
              * **HTTPS_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
               
              * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
               
              * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .  
               
              * **CALCULATED** : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .  
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

              
            

            - **ResourcePath** *(string) --* 

              The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. 

              
            

            - **FullyQualifiedDomainName** *(string) --* 

              Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

               

               **If you specify a value for**  ``IPAddress`` :

               

              Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks.

               

              When Amazon Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

               

               
              * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.  
               
              * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
               
              * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Amazon Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. 
               

               

              If you don't specify a value for ``FullyQualifiedDomainName`` , Amazon Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

               

               **If you don't specify a value for ``IPAddress`` ** :

               

              Amazon Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Amazon Route 53 then checks the health of the endpoint.

               

              .. note::

                 

                If you don't specify a value for ``IPAddress`` , Amazon Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

                 

               

              If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

               

              .. warning::

                 

                In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

                 

               

              In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Amazon Route 53 doesn't pass a ``Host`` header.

              
            

            - **SearchString** *(string) --* 

              If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.

               

              Amazon Route 53 considers case when searching for ``SearchString`` in the response body. 

              
            

            - **RequestInterval** *(integer) --* 

              The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Amazon Route 53 health checker makes requests at this interval.

               

              .. warning::

                 

                You can't change the value of ``RequestInterval`` after you create a health check.

                 

               

              If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

              
            

            - **FailureThreshold** *(integer) --* 

              The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

              
            

            - **MeasureLatency** *(boolean) --* 

              Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Amazon Route 53 console.

               

              .. warning::

                 

                You can't change the value of ``MeasureLatency`` after you create a health check.

                 

              
            

            - **Inverted** *(boolean) --* 

              Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

              
            

            - **HealthThreshold** *(integer) --* 

              The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.

               

              Note the following:

               

               
              * If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy. 
               
              * If you specify ``0`` , Amazon Route 53 always considers this health check to be healthy. 
               

              
            

            - **ChildHealthChecks** *(list) --* 

              (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

              
              

              - *(string) --* 
          
            

            - **EnableSNI** *(boolean) --* 

              Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

               

              Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

               

              The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

              
            

            - **Regions** *(list) --* 

              A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

               

              If you don't specify any regions, Amazon Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .

               

              If you update a health check to remove a region that has been performing health checks, Amazon Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions). 

              
              

              - *(string) --* 
          
            

            - **AlarmIdentifier** *(dict) --* 

              A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

              
              

              - **Region** *(string) --* 

                A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                 

                For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

                
              

              - **Name** *(string) --* 

                The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                
          
            

            - **InsufficientDataHealthStatus** *(string) --* 

              When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

               

               
              * ``Healthy`` : Amazon Route 53 considers the health check to be healthy. 
               
              * ``Unhealthy`` : Amazon Route 53 considers the health check to be unhealthy. 
               
              * ``LastKnownStatus`` : Amazon Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
               

              
        
          

          - **HealthCheckVersion** *(integer) --* 

            The version of the health check. You can optionally pass this value in a call to ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

            
          

          - **CloudWatchAlarmConfiguration** *(dict) --* 

            A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

            
            

            - **EvaluationPeriods** *(integer) --* 

              For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

              
            

            - **Threshold** *(float) --* 

              For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

              
            

            - **ComparisonOperator** *(string) --* 

              For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

              
            

            - **Period** *(integer) --* 

              For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

              
            

            - **MetricName** *(string) --* 

              The name of the CloudWatch metric that the alarm is associated with.

              
            

            - **Namespace** *(string) --* 

              The namespace of the metric that the alarm is associated with. For more information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

              
            

            - **Statistic** *(string) --* 

              For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

              
            

            - **Dimensions** *(list) --* 

              For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

              
              

              - *(dict) --* 

                For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

                
                

                - **Name** *(string) --* 

                  For the metric that the CloudWatch alarm is associated with, the name of one dimension.

                  
                

                - **Value** *(string) --* 

                  For the metric that the CloudWatch alarm is associated with, the value of one dimension.

                  
            
          
        
      
    

  .. py:method:: update_hosted_zone_comment(**kwargs)

    

    Updates the comment for a specified hosted zone.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/UpdateHostedZoneComment>`_    


    **Request Syntax** 
    ::

      response = client.update_hosted_zone_comment(
          Id='string',
          Comment='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID for the hosted zone that you want to update the comment for.

      

    
    :type Comment: string
    :param Comment: 

      The new comment for the hosted zone. If you don't specify a value for ``Comment`` , Amazon Route 53 deletes the existing value of the ``Comment`` element, if any.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZone': {
                'Id': 'string',
                'Name': 'string',
                'CallerReference': 'string',
                'Config': {
                    'Comment': 'string',
                    'PrivateZone': True|False
                },
                'ResourceRecordSetCount': 123,
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to the ``UpdateHostedZoneComment`` request.

        
        

        - **HostedZone** *(dict) --* 

          A complex type that contains general information about the hosted zone.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the hosted zone when you created it.

            
          

          - **Name** *(string) --* 

            The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

             

            For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see  CreateHostedZone .

            
          

          - **CallerReference** *(string) --* 

            The value that you specified for ``CallerReference`` when you created the hosted zone.

            
          

          - **Config** *(dict) --* 

            A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and ``Comment`` elements don't appear in the response.

            
            

            - **Comment** *(string) --* 

              Any comments that you want to include about the hosted zone.

              
            

            - **PrivateZone** *(boolean) --* 

              A value that indicates whether this is a private hosted zone.

              
        
          

          - **ResourceRecordSetCount** *(integer) --* 

            The number of resource record sets in the hosted zone.

            
          

          - **LinkedService** *(dict) --* 

            If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Amazon Route 53. 

            
            

            - **ServicePrincipal** *(string) --* 

              If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
            

            - **Description** *(string) --* 

              If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

              
        
      
    

  .. py:method:: update_traffic_policy_comment(**kwargs)

    

    Updates the comment for a specified traffic policy version.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/UpdateTrafficPolicyComment>`_    


    **Request Syntax** 
    ::

      response = client.update_traffic_policy_comment(
          Id='string',
          Version=123,
          Comment='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The value of ``Id`` for the traffic policy that you want to update the comment for.

      

    
    :type Version: integer
    :param Version: **[REQUIRED]** 

      The value of ``Version`` for the traffic policy that you want to update the comment for.

      

    
    :type Comment: string
    :param Comment: **[REQUIRED]** 

      The new comment for the specified traffic policy and version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicy': {
                'Id': 'string',
                'Version': 123,
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                'Document': 'string',
                'Comment': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response information for the traffic policy.

        
        

        - **TrafficPolicy** *(dict) --* 

          A complex type that contains settings for the specified traffic policy.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to a traffic policy when you created it.

            
          

          - **Version** *(integer) --* 

            The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of ``Version`` is always 1.

            
          

          - **Name** *(string) --* 

            The name that you specified when you created the traffic policy.

            
          

          - **Type** *(string) --* 

            The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

            
          

          - **Document** *(string) --* 

            The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the JSON format, see `Traffic Policy Document Format <http://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__ .

            
          

          - **Comment** *(string) --* 

            The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

            
      
    

  .. py:method:: update_traffic_policy_instance(**kwargs)

    

    Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.

     

    When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Amazon Route 53 performs the following operations:

     

     
    * Amazon Route 53 creates a new group of resource record sets based on the specified traffic policy. This is true regardless of how significant the differences are between the existing resource record sets and the new resource record sets.  
     
    * When all of the new resource record sets have been created, Amazon Route 53 starts to respond to DNS queries for the root resource record set name (such as example.com) by using the new resource record sets. 
     
    * Amazon Route 53 deletes the old group of resource record sets that are associated with the root resource record set name. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/UpdateTrafficPolicyInstance>`_    


    **Request Syntax** 
    ::

      response = client.update_traffic_policy_instance(
          Id='string',
          TTL=123,
          TrafficPolicyId='string',
          TrafficPolicyVersion=123
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the traffic policy instance that you want to update.

      

    
    :type TTL: integer
    :param TTL: **[REQUIRED]** 

      The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.

      

    
    :type TrafficPolicyId: string
    :param TrafficPolicyId: **[REQUIRED]** 

      The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.

      

    
    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: **[REQUIRED]** 

      The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrafficPolicyInstance': {
                'Id': 'string',
                'HostedZoneId': 'string',
                'Name': 'string',
                'TTL': 123,
                'State': 'string',
                'Message': 'string',
                'TrafficPolicyId': 'string',
                'TrafficPolicyVersion': 123,
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains information about the resource record sets that Amazon Route 53 created based on a specified traffic policy.

        
        

        - **TrafficPolicyInstance** *(dict) --* 

          A complex type that contains settings for the updated traffic policy instance.

          
          

          - **Id** *(string) --* 

            The ID that Amazon Route 53 assigned to the new traffic policy instance.

            
          

          - **HostedZoneId** *(string) --* 

            The ID of the hosted zone that Amazon Route 53 created resource record sets in.

            
          

          - **Name** *(string) --* 

            The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance. 

            
          

          - **TTL** *(integer) --* 

            The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

            
          

          - **State** *(string) --* 

            The value of ``State`` is one of the following values:

              Applied  

            Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Amazon Route 53 edge locations.

              Creating  

            Amazon Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

              Failed  

            Amazon Route 53 wasn't able to create or update the resource record sets. When the value of ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to fail.

              
          

          - **Message** *(string) --* 

            If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is another value, ``Message`` is empty.

            
          

          - **TrafficPolicyId** *(string) --* 

            The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

            
          

          - **TrafficPolicyVersion** *(integer) --* 

            The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

            
          

          - **TrafficPolicyType** *(string) --* 

            The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance. 

            
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`Route53.Paginator.ListHealthChecks`


* :py:class:`Route53.Paginator.ListHostedZones`


* :py:class:`Route53.Paginator.ListResourceRecordSets`



.. py:class:: Route53.Paginator.ListHealthChecks

  ::

    
    paginator = client.get_paginator('list_health_checks')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Route53.Client.list_health_checks`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHealthChecks>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HealthChecks': [
                {
                    'Id': 'string',
                    'CallerReference': 'string',
                    'LinkedService': {
                        'ServicePrincipal': 'string',
                        'Description': 'string'
                    },
                    'HealthCheckConfig': {
                        'IPAddress': 'string',
                        'Port': 123,
                        'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                        'ResourcePath': 'string',
                        'FullyQualifiedDomainName': 'string',
                        'SearchString': 'string',
                        'RequestInterval': 123,
                        'FailureThreshold': 123,
                        'MeasureLatency': True|False,
                        'Inverted': True|False,
                        'HealthThreshold': 123,
                        'ChildHealthChecks': [
                            'string',
                        ],
                        'EnableSNI': True|False,
                        'Regions': [
                            'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                        ],
                        'AlarmIdentifier': {
                            'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                            'Name': 'string'
                        },
                        'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
                    },
                    'HealthCheckVersion': 123,
                    'CloudWatchAlarmConfiguration': {
                        'EvaluationPeriods': 123,
                        'Threshold': 123.0,
                        'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                        'Period': 123,
                        'MetricName': 'string',
                        'Namespace': 'string',
                        'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
            ],
            'Marker': 'string',
            'IsTruncated': True|False,
            'MaxItems': 'string',
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains the response to a ``ListHealthChecks`` request.

        
        

        - **HealthChecks** *(list) --* 

          A complex type that contains one ``HealthCheck`` element for each health check that is associated with the current AWS account.

          
          

          - *(dict) --* 

            A complex type that contains information about one health check that is associated with the current AWS account.

            
            

            - **Id** *(string) --* 

              The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. 

              
            

            - **CallerReference** *(string) --* 

              A unique string that you specified when you created the health check.

              
            

            - **LinkedService** *(dict) --* 

              If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can't edit or delete it using Amazon Route 53. 

              
              

              - **ServicePrincipal** *(string) --* 

                If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
              

              - **Description** *(string) --* 

                If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
          
            

            - **HealthCheckConfig** *(dict) --* 

              A complex type that contains detailed information about one health check.

              
              

              - **IPAddress** *(string) --* 

                The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Amazon Route 53 then checks the health of the endpoint.

                 

                Use one of the following formats for the value of ``IPAddress`` : 

                 

                 
                * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
                 
                * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
                 

                 

                If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.

                 

                For more information, see  HealthCheckConfig$FullyQualifiedDomainName .

                 

                Constraints: Amazon Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

                 

                 
                * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
                 
                * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
                 
                * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
                 

                 

                When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

                
              

              - **Port** *(integer) --* 

                The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

                
              

              - **Type** *(string) --* 

                The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

                 

                .. warning::

                   

                  You can't change the value of ``Type`` after you create a health check.

                   

                 

                You can create the following types of health checks:

                 

                 
                * **HTTP** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
                 
                * **HTTPS** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 

                .. warning::

                   If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 

                 
                 
                * **HTTP_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
                 
                * **HTTPS_STR_MATCH** : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
                 
                * **TCP** : Amazon Route 53 tries to establish a TCP connection. 
                 
                * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .  
                 
                * **CALCULATED** : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .  
                 

                 

                For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

                
              

              - **ResourcePath** *(string) --* 

                The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. 

                
              

              - **FullyQualifiedDomainName** *(string) --* 

                Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

                 

                 **If you specify a value for**  ``IPAddress`` :

                 

                Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks.

                 

                When Amazon Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

                 

                 
                * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.  
                 
                * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
                 
                * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Amazon Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. 
                 

                 

                If you don't specify a value for ``FullyQualifiedDomainName`` , Amazon Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

                 

                 **If you don't specify a value for ``IPAddress`` ** :

                 

                Amazon Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Amazon Route 53 then checks the health of the endpoint.

                 

                .. note::

                   

                  If you don't specify a value for ``IPAddress`` , Amazon Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

                   

                 

                If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

                 

                .. warning::

                   

                  In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

                   

                 

                In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Amazon Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Amazon Route 53 doesn't pass a ``Host`` header.

                
              

              - **SearchString** *(string) --* 

                If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.

                 

                Amazon Route 53 considers case when searching for ``SearchString`` in the response body. 

                
              

              - **RequestInterval** *(integer) --* 

                The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Amazon Route 53 health checker makes requests at this interval.

                 

                .. warning::

                   

                  You can't change the value of ``RequestInterval`` after you create a health check.

                   

                 

                If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

                
              

              - **FailureThreshold** *(integer) --* 

                The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .

                 

                If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

                
              

              - **MeasureLatency** *(boolean) --* 

                Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Amazon Route 53 console.

                 

                .. warning::

                   

                  You can't change the value of ``MeasureLatency`` after you create a health check.

                   

                
              

              - **Inverted** *(boolean) --* 

                Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

                
              

              - **HealthThreshold** *(integer) --* 

                The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.

                 

                Note the following:

                 

                 
                * If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy. 
                 
                * If you specify ``0`` , Amazon Route 53 always considers this health check to be healthy. 
                 

                
              

              - **ChildHealthChecks** *(list) --* 

                (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

                
                

                - *(string) --* 
            
              

              - **EnableSNI** *(boolean) --* 

                Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

                 

                Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

                 

                The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

                
              

              - **Regions** *(list) --* 

                A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

                 

                If you don't specify any regions, Amazon Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .

                 

                If you update a health check to remove a region that has been performing health checks, Amazon Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions). 

                
                

                - *(string) --* 
            
              

              - **AlarmIdentifier** *(dict) --* 

                A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                
                

                - **Region** *(string) --* 

                  A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                   

                  For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

                  
                

                - **Name** *(string) --* 

                  The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

                  
            
              

              - **InsufficientDataHealthStatus** *(string) --* 

                When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

                 

                 
                * ``Healthy`` : Amazon Route 53 considers the health check to be healthy. 
                 
                * ``Unhealthy`` : Amazon Route 53 considers the health check to be unhealthy. 
                 
                * ``LastKnownStatus`` : Amazon Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
                 

                
          
            

            - **HealthCheckVersion** *(integer) --* 

              The version of the health check. You can optionally pass this value in a call to ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

              
            

            - **CloudWatchAlarmConfiguration** *(dict) --* 

              A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

              
              

              - **EvaluationPeriods** *(integer) --* 

                For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

                
              

              - **Threshold** *(float) --* 

                For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

                
              

              - **ComparisonOperator** *(string) --* 

                For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

                
              

              - **Period** *(integer) --* 

                For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

                
              

              - **MetricName** *(string) --* 

                The name of the CloudWatch metric that the alarm is associated with.

                
              

              - **Namespace** *(string) --* 

                The namespace of the metric that the alarm is associated with. For more information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

                
              

              - **Statistic** *(string) --* 

                For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

                
              

              - **Dimensions** *(list) --* 

                For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .

                
                

                - *(dict) --* 

                  For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

                  
                  

                  - **Name** *(string) --* 

                    For the metric that the CloudWatch alarm is associated with, the name of one dimension.

                    
                  

                  - **Value** *(string) --* 

                    For the metric that the CloudWatch alarm is associated with, the value of one dimension.

                    
              
            
          
        
      
        

        - **Marker** *(string) --* 

          For the second and subsequent calls to ``ListHealthChecks`` , ``Marker`` is the value that you specified for the ``marker`` parameter in the previous request.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether there are more health checks to be listed. If the response was truncated, you can get the next group of health checks by submitting another ``ListHealthChecks`` request and specifying the value of ``NextMarker`` in the ``marker`` parameter.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``maxitems`` parameter in the call to ``ListHealthChecks`` that produced the current response.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Route53.Paginator.ListHostedZones

  ::

    
    paginator = client.get_paginator('list_hosted_zones')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Route53.Client.list_hosted_zones`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHostedZones>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DelegationSetId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type DelegationSetId: string
    :param DelegationSetId: 

      If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set. 

      

    
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'HostedZones': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'CallerReference': 'string',
                    'Config': {
                        'Comment': 'string',
                        'PrivateZone': True|False
                    },
                    'ResourceRecordSetCount': 123,
                    'LinkedService': {
                        'ServicePrincipal': 'string',
                        'Description': 'string'
                    }
                },
            ],
            'Marker': 'string',
            'IsTruncated': True|False,
            'MaxItems': 'string',
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **HostedZones** *(list) --* 

          A complex type that contains general information about the hosted zone.

          
          

          - *(dict) --* 

            A complex type that contains general information about the hosted zone.

            
            

            - **Id** *(string) --* 

              The ID that Amazon Route 53 assigned to the hosted zone when you created it.

              
            

            - **Name** *(string) --* 

              The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

               

              For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see  CreateHostedZone .

              
            

            - **CallerReference** *(string) --* 

              The value that you specified for ``CallerReference`` when you created the hosted zone.

              
            

            - **Config** *(dict) --* 

              A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and ``Comment`` elements don't appear in the response.

              
              

              - **Comment** *(string) --* 

                Any comments that you want to include about the hosted zone.

                
              

              - **PrivateZone** *(boolean) --* 

                A value that indicates whether this is a private hosted zone.

                
          
            

            - **ResourceRecordSetCount** *(integer) --* 

              The number of resource record sets in the hosted zone.

              
            

            - **LinkedService** *(dict) --* 

              If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Amazon Route 53. 

              
              

              - **ServicePrincipal** *(string) --* 

                If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
              

              - **Description** *(string) --* 

                If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. 

                
          
        
      
        

        - **Marker** *(string) --* 

          For the second and subsequent calls to ``ListHostedZones`` , ``Marker`` is the value that you specified for the ``marker`` parameter in the request that produced the current response.

          
        

        - **IsTruncated** *(boolean) --* 

          A flag indicating whether there are more hosted zones to be listed. If the response was truncated, you can get more hosted zones by submitting another ``ListHostedZones`` request and specifying the value of ``NextMarker`` in the ``marker`` parameter.

          
        

        - **MaxItems** *(string) --* 

          The value that you specified for the ``maxitems`` parameter in the call to ``ListHostedZones`` that produced the current response.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Route53.Paginator.ListResourceRecordSets

  ::

    
    paginator = client.get_paginator('list_resource_record_sets')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Route53.Client.list_resource_record_sets`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListResourceRecordSets>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          HostedZoneId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type HostedZoneId: string
    :param HostedZoneId: **[REQUIRED]** 

      The ID of the hosted zone that contains the resource record sets that you want to list.

      

    
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceRecordSets': [
                {
                    'Name': 'string',
                    'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                    'SetIdentifier': 'string',
                    'Weight': 123,
                    'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-west-1'|'eu-west-2'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                    'GeoLocation': {
                        'ContinentCode': 'string',
                        'CountryCode': 'string',
                        'SubdivisionCode': 'string'
                    },
                    'Failover': 'PRIMARY'|'SECONDARY',
                    'MultiValueAnswer': True|False,
                    'TTL': 123,
                    'ResourceRecords': [
                        {
                            'Value': 'string'
                        },
                    ],
                    'AliasTarget': {
                        'HostedZoneId': 'string',
                        'DNSName': 'string',
                        'EvaluateTargetHealth': True|False
                    },
                    'HealthCheckId': 'string',
                    'TrafficPolicyInstanceId': 'string'
                },
            ],
            'IsTruncated': True|False,
            'MaxItems': 'string',
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A complex type that contains list information for the resource record set.

        
        

        - **ResourceRecordSets** *(list) --* 

          Information about multiple resource record sets.

          
          

          - *(dict) --* 

            Information about the resource record set to create or delete.

            
            

            - **Name** *(string) --* 

              The name of the domain you want to perform the action on.

               

              Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical.

               

              For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following:

               

               
              * The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` . 
               
              * The * can't replace any of the middle labels, for example, marketing.*.example.com. 
               
              * If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. 

              .. warning::

                 You can't use the * wildcard for resource records sets that have a type of NS. 

               
               

               

              You can use the * wildcard as the leftmost label in a domain name, for example, ``*.example.com`` . You can't use an * for one of the middle labels, for example, ``marketing.*.example.com`` . In addition, the * must replace the entire label; for example, you can't specify ``prod*.example.com`` .

              
            

            - **Type** *(string) --* 

              The DNS record type. For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .

               

              Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``  

               

              Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.

               

              Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``  

               

              .. note::

                 

                SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <http://tools.ietf.org/html/rfc7208#section-14.1>`__ .

                 

               

              Values for alias resource record sets:

               

               
              * **CloudFront distributions:**  ``A``   If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` .  
               
              * **AWS Elastic Beanstalk environment that has a regionalized subdomain** : ``A``   
               
              * **ELB load balancers:**  ``A`` | ``AAAA``   
               
              * **Amazon S3 buckets:**  ``A``   
               
              * **Another resource record set in this hosted zone:** Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` . 
               

              
            

            - **SetIdentifier** *(string) --* 

               *Weighted, Latency, Geo, and Failover resource record sets only:* An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of ``SetIdentifier`` must be unique for each resource record set that has the same combination of DNS name and type. Omit ``SetIdentifier`` for any other types of record sets.

              
            

            - **Weight** *(integer) --* 

               *Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Amazon Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Amazon Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:

               

               
              * You must specify a value for the ``Weight`` element for every weighted resource record set. 
               
              * You can only specify one ``ResourceRecord`` per weighted resource record set. 
               
              * You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets. 
               
              * You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements. 
               
              * For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Amazon Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Amazon Route 53 Active-Active and Active-Passive Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`__ in the *Amazon Route 53 Developer Guide* . 
               

              
            

            - **Region** *(string) --* 

               *Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.

               

              .. note::

                 

                Creating latency and latency alias resource record sets in private hosted zones is not supported.

                 

               

              When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Amazon Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Amazon Route 53 then returns the value that is associated with the selected resource record set.

               

              Note the following:

               

               
              * You can only specify one ``ResourceRecord`` per latency resource record set. 
               
              * You can only create one latency resource record set for each Amazon EC2 Region. 
               
              * You aren't required to create latency resource record sets for all Amazon EC2 Regions. Amazon Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for. 
               
              * You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets. 
               

              
            

            - **GeoLocation** *(dict) --* 

               *Geo location resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` .

               

              .. note::

                 

                Creating geolocation and geolocation alias resource record sets in private hosted zones is not supported.

                 

               

              If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.

               

              You can't create two geolocation resource record sets that specify the same geographic location.

               

              The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements.

               

              .. warning::

                 

                Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Amazon Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` , which handles both queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Amazon Route 53 returns a "no answer" response for queries from those locations.

                 

               

              You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.

              
              

              - **ContinentCode** *(string) --* 

                The two-letter code for the continent.

                 

                Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``  

                 

                Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.

                
              

              - **CountryCode** *(string) --* 

                The two-letter code for the country.

                
              

              - **SubdivisionCode** *(string) --* 

                The code for the subdivision, for example, a state in the United States or a province in Canada.

                
          
            

            - **Failover** *(string) --* 

               *Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets. For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set.

               

              Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets:

               

               
              * When the primary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. 
               
              * When the primary resource record set is unhealthy and the secondary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the secondary resource record set. 
               
              * When the secondary resource record set is unhealthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. 
               
              * If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Amazon Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. 
               

               

              You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets.

               

              For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true.

               

              For more information about configuring failover for Amazon Route 53, see the following topics in the *Amazon Route 53 Developer Guide* : 

               

               
              * `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
               
              * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
               

              
            

            - **MultiValueAnswer** *(boolean) --* 

               *Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` . Note the following:

               

               
              * If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. 
               
              * If you don't associate a health check with a multivalue answer record, Amazon Route 53 always considers the record to be healthy. 
               
              * Amazon Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Amazon Route 53 responds to all DNS queries with all the healthy records. 
               
              * If you have more than eight healthy records, Amazon Route 53 responds to different DNS resolvers with different combinations of healthy records. 
               
              * When all records are unhealthy, Amazon Route 53 responds to DNS queries with up to eight unhealthy records. 
               
              * If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. 
               

               

              You can't create multivalue answer alias records.

              
            

            - **TTL** *(integer) --* 

              The resource record cache time to live (TTL), in seconds. Note the following:

               

               
              * If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target.  
               
              * If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status. 
               
              * All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` . 
               
              * If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` . 
               

              
            

            - **ResourceRecords** *(list) --* 

              Information about the resource records to act upon.

               

              .. note::

                 

                If you're creating an alias resource record set, omit ``ResourceRecords`` .

                 

              
              

              - *(dict) --* 

                Information specific to the resource record.

                 

                .. note::

                   

                  If you're creating an alias resource record set, omit ``ResourceRecord`` .

                   

                
                

                - **Value** *(string) --* 

                  The current or new DNS record value, not to exceed 4,000 characters. In the case of a ``DELETE`` action, if the current value does not match the actual value, an error is returned. For descriptions about how to format ``Value`` for different record types, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .

                   

                  You can specify more than one value for all record types except ``CNAME`` and ``SOA`` . 

                   

                  .. note::

                     

                    If you're creating an alias resource record set, omit ``Value`` .

                     

                  
            
          
            

            - **AliasTarget** *(dict) --* 

               *Alias resource record sets only:* Information about the CloudFront distribution, AWS Elastic Beanstalk environment, ELB load balancer, Amazon S3 bucket, or Amazon Route 53 resource record set to which you're redirecting queries. The AWS Elastic Beanstalk environment must have a regionalized subdomain.

               

              If you're creating resource records sets for a private hosted zone, note the following:

               

               
              * You can't create alias resource record sets for CloudFront distributions in a private hosted zone. 
               
              * Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported. 
               
              * For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__ in the *Amazon Route 53 Developer Guide* . 
               

              
              

              - **HostedZoneId** *(string) --* 

                 *Alias resource records sets only* : The value used depends on where you want to route traffic:

                  CloudFront distribution  

                Specify ``Z2FDTNDATAQYW2`` .

                 

                .. note::

                   

                  Alias resource record sets for CloudFront can't be created in a private zone.

                   

                  Elastic Beanstalk environment  

                Specify the hosted zone ID for the region in which you created the environment. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk <http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region>`__ in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* .

                  ELB load balancer  

                Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:

                 

                 
                * `Elastic Load Balancing <http://docs.aws.amazon.com/general/latest/gr/rande.html#elb_region>`__ table in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers. 
                 
                * **AWS Management Console** : Go to the Amazon EC2 page, choose **Load Balancers** in the navigation pane, select the load balancer, and get the value of the **Hosted zone** field on the **Description** tab. 
                 
                * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                   
                  * Application and Network Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                   

                 
                 
                * **AWS CLI** : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                   
                  * Application and Network Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                   

                 
                 

                  An Amazon S3 bucket configured as a static website  

                Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the `Amazon Simple Storage Service Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ table in the "AWS Regions and Endpoints" chapter of the *Amazon Web Services General Reference* .

                  Another Amazon Route 53 resource record set in your hosted zone  

                Specify the hosted zone ID of your hosted zone. (An alias resource record set can't reference a resource record set in a different hosted zone.)

                  
              

              - **DNSName** *(string) --* 

                 *Alias resource record sets only:* The value that you specify depends on where you want to route queries:

                  CloudFront distribution  

                Specify the domain name that CloudFront assigned when you created your distribution.

                 

                Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`__ in the *Amazon CloudFront Developer Guide* .

                  Elastic Beanstalk environment  

                Specify the ``CNAME`` attribute for the environment. (The environment must have a regionalized domain name.) You can use the following methods to get the value of the CNAME attribute:

                 

                 
                * *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 
                 
                * *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`__ in the *AWS Elastic Beanstalk API Reference* . 
                 
                * *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <http://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`__ in the *AWS Command Line Interface Reference* . 
                 

                  ELB load balancer  

                Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. 

                 

                 
                * **AWS Management Console** : Go to the EC2 page, choose **Load Balancers** in the navigation pane, choose the load balancer, choose the **Description** tab, and get the value of the **DNS name** field. (If you're routing traffic to a Classic Load Balancer, get the value that begins with **dualstack** .)  
                 
                * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__   
                   
                  * Application and Network Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__   
                   

                 
                 
                * **AWS CLI** : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 

                   
                  * Classic Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__   
                   
                  * Application and Network Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__   
                   

                 
                 

                  Amazon S3 bucket that is configured as a static website  

                Specify the domain name of the Amazon S3 website endpoint in which you created the bucket, for example, ``s3-website-us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon Simple Storage Service (S3) Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`__ in the *Amazon Route 53 Developer Guide.*  

                  Another Amazon Route 53 resource record set  

                Specify the value of the ``Name`` element for a resource record set in the current hosted zone.

                  
              

              - **EvaluateTargetHealth** *(boolean) --* 

                 *Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets:* When ``EvaluateTargetHealth`` is ``true`` , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer, or the referenced resource record set.

                 

                Note the following:

                 

                 
                * You can't set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution. 
                 
                * If the AWS resource that you specify in ``AliasTarget`` is a resource record set or a group of resource record sets (for example, a group of weighted resource record sets), but it is not another alias resource record set, we recommend that you associate a health check with all of the resource record sets in the alias target. For more information, see `What Happens When You Omit Health Checks? <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`__ in the *Amazon Route 53 Developer Guide* . 
                 
                * If you specify an Elastic Beanstalk environment in ``HostedZoneId`` and ``DNSName`` , and if the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Amazon Route 53 routes queries to other available resources that are healthy, if any. If the environment contains a single EC2 instance, there are no special requirements. 
                 
                * If you specify an ELB load balancer in ``  AliasTarget `` , ELB routes queries only to the healthy EC2 instances that are registered with the load balancer. If no EC2 instances are healthy or if the load balancer itself is unhealthy, and if ``EvaluateTargetHealth`` is true for the corresponding alias resource record set, Amazon Route 53 routes queries to other resources. When you create a load balancer, you configure settings for ELB health checks; they're not Amazon Route 53 health checks, but they perform a similar function. Do not create Amazon Route 53 health checks for the EC2 instances that you register with an ELB load balancer. For more information, see `How Health Checks Work in More Complex Amazon Route 53 Configurations <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html>`__ in the *Amazon Route 53 Developer Guide* . 
                 
                * We recommend that you set ``EvaluateTargetHealth`` to true only when you have enough idle capacity to handle the failure of one or more endpoints. 
                 

                 

                For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__ in the *Amazon Route 53 Developer Guide* .

                
          
            

            - **HealthCheckId** *(string) --* 

              If you want Amazon Route 53 to return this resource record set in response to a DNS query only when a health check is passing, include the ``HealthCheckId`` element and specify the ID of the applicable health check.

               

              Amazon Route 53 determines whether a resource record set is healthy based on one of the following:

               

               
              * By periodically sending a request to the endpoint that is specified in the health check 
               
              * By aggregating the status of a specified group of health checks (calculated health checks) 
               
              * By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) 
               

               

              For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ .

               

              The ``HealthCheckId`` element is only useful when Amazon Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Amazon Route 53 to base the choice in part on the status of a health check. Configuring health checks only makes sense in the following configurations:

               

               
              * You're checking the health of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets, and you specify health check IDs for all of the resource record sets. If the health check for one resource record set specifies an endpoint that is not healthy, Amazon Route 53 stops responding to queries using the value for that resource record set. 
               
              * You set ``EvaluateTargetHealth`` to true for the resource record sets in a group of alias, weighted alias, latency alias, geolocation alias, or failover alias resource record sets, and you specify health check IDs for all of the resource record sets that are referenced by the alias resource record sets. 
               

               

              .. warning::

                 

                Amazon Route 53 doesn't check the health of the endpoint specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Amazon Route 53 checks the health of the endpoint that you specified in the health check. 

                 

               

              For geolocation resource record sets, if an endpoint is unhealthy, Amazon Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the United States, for North America, and for all locations. If the endpoint for the state resource record set is unhealthy, Amazon Route 53 checks the resource record sets for the United States, for North America, and for all locations (a resource record set for which the value of ``CountryCode`` is ``*`` ), in that order, until it finds a resource record set for which the endpoint is healthy. 

               

              If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets (example.com).

               

              .. warning::

                 

                n this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and then associate the health check with those resource record sets, health check results will be unpredictable.

                 

               

              For more information, see the following topics in the *Amazon Route 53 Developer Guide* :

               

               
              * `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
               
              * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
               

              
            

            - **TrafficPolicyInstanceId** *(string) --* 

              When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. ``TrafficPolicyInstanceId`` is the ID of the traffic policy instance that Amazon Route 53 created this resource record set for.

               

              .. warning::

                 

                To delete the resource record set that is associated with a traffic policy instance, use ``DeleteTrafficPolicyInstance`` . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ``ChangeResourceRecordSets`` , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use. 

                 

              
        
      
        

        - **IsTruncated** *(boolean) --* 

          A flag that indicates whether more resource record sets remain to be listed. If your results were truncated, you can make a follow-up pagination request by using the ``NextRecordName`` element.

          
        

        - **MaxItems** *(string) --* 

          The maximum number of records you requested.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

=======
Waiters
=======


The available waiters are:

* :py:class:`Route53.Waiter.ResourceRecordSetsChanged`



.. py:class:: Route53.Waiter.ResourceRecordSetsChanged

  ::

    
    waiter = client.get_waiter('resource_record_sets_changed')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`Route53.Client.get_change` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetChange>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          Id='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID of the change batch request. The value that you specify here is the value that ``ChangeResourceRecordSets`` returned in the ``Id`` element when you submitted the request.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None