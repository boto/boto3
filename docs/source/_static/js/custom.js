/*
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
const nonResourceSubHeadings = [
	'client',
	'waiters',
	'paginators',
	'resources',
	'examples'
];
// Checks if an html doc name matches a service class name.
function isValidServiceName(serviceClassName) {
	const pageTitle = document.getElementsByTagName('h1')[0];
	const newDocName = pageTitle.innerText.replace('#', '');
	return newDocName.toLowerCase() === serviceClassName;
}
// Checks if all elements of the split fragment are valid.
// Fragment items should only contain alphanumerics, hyphens, & underscores.
// A fragment should also only be redirected if it contain 3-5 items.
function isValidFragment(splitFragment) {
	const regex = /^[a-z0-9-_]+$/i;
	for (index in splitFragment) {
		if (!regex.test(splitFragment[index])) {
			return false;
		}
	}
	return splitFragment.length >= 1 && splitFragment.length < 5;
}
// Checks if a name is a possible resource name.
function isValidResource(name, serviceDocName) {
	return name.replaceAll('-', '') !== serviceDocName && !nonResourceSubHeadings.includes(name);
}
// Reroutes previously existing links to the new path.
// Old: <root_url>/reference/services/s3.html#S3.Client.delete_bucket
// New: <root_url>/reference/services/s3/client/delete_bucket.html
// This must be done client side since the fragment (#S3.Client.delete_bucket) is never
// passed to the server.
(function () {
	const currentPath = window.location.pathname.split('/');
	const fragment = window.location.hash.substring(1);
	const splitFragment = fragment.split('.').map(part => part.replace(/serviceresource/i, 'service-resource'));
	// Only redirect when viewing a top-level service page.
	if (isValidFragment(splitFragment) && currentPath[currentPath.length - 2] === 'services') {
		const serviceDocName = currentPath[currentPath.length - 1].replace('.html', '');
		if (splitFragment.length > 1) {
			splitFragment[0] = splitFragment[0].toLowerCase();
			splitFragment[1] = splitFragment[1].toLowerCase();
		}
		let newPath;
		if (splitFragment.length >= 3 && isValidServiceName(splitFragment[0])) {
			splitFragment[0] = serviceDocName;
			newPath = `${ splitFragment.slice(0, 3).join('/') }.html#${ splitFragment.length > 3 ? fragment : '' }`;
		} else if (splitFragment.length == 2 && isValidResource(splitFragment[1].toLowerCase(), serviceDocName)) {
			newPath = `${ splitFragment.join('/') }/index.html#${ fragment }`;
		} else if (splitFragment.length == 1 && isValidResource(splitFragment[0], serviceDocName)) {
			newPath = `${ serviceDocName }/${ splitFragment.join('/') }/index.html`;
		} else {
			return;
		}
		window.location.assign(newPath);
	}
}());
// Given a service name, we apply the html classes which indicate a current page to the corresponsing list item.
// Before: <li class="toctree-l2"><a class="reference internal" href="../../acm.html">ACM</a></li>
// After: <li class="toctree-l2 current current-page"><a class="reference internal" href="../../acm.html">ACM</a></li>
function makeServiceLinkCurrent(serviceName) {
	const servicesSection = [...document.querySelectorAll('a')].find(
		e => e.innerHTML.includes('Available Services')
	).parentElement;
	var linkElement = servicesSection.querySelectorAll(`a[href*="../${ serviceName }.html"]`);
	if (linkElement.length === 0) {
		linkElement = servicesSection.querySelectorAll(`a[href="#"]`)[0];
	} else {
		linkElement = linkElement[0];
	}
	let linkParent = linkElement.parentElement;
	linkParent.classList.add('current');
	linkParent.classList.add('current-page');
}
const currentPagePath = window.location.pathname.split('/');
const codeBlockSelector = 'div.highlight pre';
// Expands the "Available Services" sub-menu in the side-bar when viewing
// nested doc pages and highlights the corresponding service list item.
function expandSubMenu() {
	if (currentPagePath.includes('services')) {
		document.getElementById('toctree-checkbox-11').checked = true;
		// Example Nested Path: /reference/services/<service_name>/client/<operation_name>.html
		const serviceNameIndex = currentPagePath.indexOf('services') + 1;
		const serviceName = currentPagePath[serviceNameIndex];
		makeServiceLinkCurrent(serviceName);
	}
}
// Allows code blocks to be scrollable by keyboard only users.
function makeCodeBlocksScrollable() {
	const codeCells = document.querySelectorAll(codeBlockSelector);
	codeCells.forEach(codeCell => {
		codeCell.tabIndex = 0;
	});
}
// Functions to run after the DOM loads.
function runAfterDOMLoads() {
	expandSubMenu();
	makeCodeBlocksScrollable();
}
// Run a function after the DOM loads.
function ready(fn) {
	if (document.readyState !== 'loading') {
		fn();
	} else {
		document.addEventListener('DOMContentLoaded', fn);
	}
}
ready(runAfterDOMLoads);
