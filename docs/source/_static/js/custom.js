// Reroutes previously existing links to the new path.
// Old: <root_url>/reference/services/s3.html#S3.Client.delete_bucket
// New: <root_url>/reference/services/s3/client/delete_bucket.html
// This must be done client side since the fragment (#S3.Client.delete_bucket) is never
// passed to the server.
(function () {
    var currentPath = window.location.pathname.split('/')
    var fragment = window.location.hash.substring(1);
    if (fragment && currentPath[currentPath.length - 2] == 'services') {
        splitFragment = fragment.split('.');
        if (splitFragment.length > 2){
            newPath = `${splitFragment.join('/')}.html`
            window.location.replace(newPath);
        }
    }
})();
