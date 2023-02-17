// Reroutes previously existing links to the new path.
// Old: <root_url>/reference/services/s3.html#S3.Client.delete_bucket
// New: <root_url>/reference/services/s3/client/delete_bucket.html
// This must be done client side since the fragment (#S3.Client.delete_bucket) is never
// passed to the server.
const nonResourceSubHeadings = [
	'client',
	'waiters',
	'paginators',
	'resources',
	'examples'
];
function isValidResource(name, serviceName) {
	return name.replace('-', '') != serviceName && !nonResourceSubHeadings.includes(name) ? true : false;
}
(function () {
	const currentPath = window.location.pathname.split('/');
	const fragment = window.location.hash.substring(1);
	// Only redirect when viewing a top-level service page.
	if (fragment && currentPath[currentPath.length - 2] === 'services') {
		const serviceName = currentPath[currentPath.length - 1].replace('.html', '');
		const splitFragment = fragment.split('.').map(part => part.replace(/serviceresource/i, 'service-resource'));
		splitFragment[0] = splitFragment[0].toLowerCase();
		let newPath = `${ splitFragment.slice(0, 3).join('/') }.html`;
		if (splitFragment.length >= 3) {
			splitFragment[1] = splitFragment[1].toLowerCase();
			newPath = splitFragment.length === 3 ? newPath : `${ newPath }#${ fragment }`;
		} else if (splitFragment.length == 2 && isValidResource(splitFragment[1].toLowerCase(), serviceName)) {
			splitFragment[1] = splitFragment[1].toLowerCase();
			newPath = splitFragment.join('/') + '/index.html#' + fragment;
		} else if (splitFragment.length == 1 && isValidResource(splitFragment[0], serviceName)) {
			newPath = [
				serviceName,
				...splitFragment,
				'index.html'
			].join('/');
		} else {
			return;
		}
		window.location.replace(newPath);
	}
}());
