/**
 * version_warning.js
 *
 * Detects when a user is viewing an outdated versioned page of the Boto3
 * documentation (e.g. /api/1.35.6/...) and injects a banner directing
 * them to the equivalent page on /api/latest/...
 */
(function () {
  "use strict";

  var LATEST_PATH_SEGMENT = "/api/latest/";

  function isVersionedPage() {
    var path = window.location.pathname;
    return /\/api\/\d+\.\d+(\.\d+)?\//i.test(path);
  }

  function buildLatestUrl() {
    var path = window.location.pathname;
    var latestPath = path.replace(
      /\/api\/\d+\.\d+(\.\d+)?\//i,
      LATEST_PATH_SEGMENT
    );
    return (
      window.location.protocol +
      "//" +
      window.location.host +
      latestPath +
      window.location.search +
      window.location.hash
    );
  }

  function injectBanner() {
    var latestUrl = buildLatestUrl();

    var banner = document.createElement("div");
    banner.id = "boto3-version-warning";
    banner.setAttribute("role", "note");
    banner.innerHTML =
      "<strong>Note:</strong> This documentation is for a past release of Boto3. " +
      'To access the latest version, please refer to ' +
      '<a href="' + latestUrl + '">this page</a>. ' +
      'To update your version of Boto3, follow the ' +
      '<a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationpy3.html#to-update-the-aws-sdk-for-python">' +
      "instructions here</a>.";

    banner.style.cssText = [
      "background: #fff3cd",
      "border: 1px solid #ffc107",
      "border-radius: 4px",
      "color: #856404",
      "font-size: 0.95em",
      "margin: 0 0 1.5em 0",
      "padding: 0.75em 1em"
    ].join(";");

    var target =
      document.getElementById("furo-main-content") ||
      document.querySelector("article[role='main']") ||
      document.querySelector(".document") ||
      document.body.firstElementChild;

    if (target) {
      target.insertBefore(banner, target.firstChild);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      if (isVersionedPage()) { injectBanner(); }
    });
  } else {
    if (isVersionedPage()) { injectBanner(); }
  }
})();
