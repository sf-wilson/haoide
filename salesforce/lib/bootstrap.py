"""
Class for bootstrap3, which is copied from https://github.com/Pleasurazy/Sublime-Better-Completion
"""
classes = [
    "container",
    "container-fluid",
    "row",

    "bg-danger",
    "bg-info",
    "bg-primary",
    "bg-success",
    "bg-warning",

    "col-xs-1",
    "col-xs-2",
    "col-xs-3",
    "col-xs-4",
    "col-xs-5",
    "col-xs-6",
    "col-xs-7",
    "col-xs-8",
    "col-xs-9",
    "col-xs-10",
    "col-xs-11",
    "col-xs-12",
    "col-sm-1",
    "col-sm-2",
    "col-sm-3",
    "col-sm-4",
    "col-sm-5",
    "col-sm-6",
    "col-sm-7",
    "col-sm-8",
    "col-sm-9",
    "col-sm-10",
    "col-sm-11",
    "col-sm-12",
    "col-md-1",
    "col-md-2",
    "col-md-3",
    "col-md-4",
    "col-md-5",
    "col-md-6",
    "col-md-7",
    "col-md-8",
    "col-md-9",
    "col-md-10",
    "col-md-11",
    "col-md-12",
    "col-lg-1",
    "col-lg-2",
    "col-lg-3",
    "col-lg-4",
    "col-lg-5",
    "col-lg-6",
    "col-lg-7",
    "col-lg-8",
    "col-lg-9",
    "col-lg-10",
    "col-lg-11",
    "col-lg-12",

    "col-xs-push-1",
    "col-xs-push-2",
    "col-xs-push-3",
    "col-xs-push-4",
    "col-xs-push-5",
    "col-xs-push-6",
    "col-xs-push-7",
    "col-xs-push-8",
    "col-xs-push-9",
    "col-xs-push-10",
    "col-xs-push-11",
    "col-sm-push-1",
    "col-sm-push-2",
    "col-sm-push-3",
    "col-sm-push-4",
    "col-sm-push-5",
    "col-sm-push-6",
    "col-sm-push-7",
    "col-sm-push-8",
    "col-sm-push-9",
    "col-sm-push-10",
    "col-sm-push-11",
    "col-md-push-1",
    "col-md-push-2",
    "col-md-push-3",
    "col-md-push-4",
    "col-md-push-5",
    "col-md-push-6",
    "col-md-push-7",
    "col-md-push-8",
    "col-md-push-9",
    "col-md-push-10",
    "col-md-push-11",
    "col-lg-push-1",
    "col-lg-push-2",
    "col-lg-push-3",
    "col-lg-push-4",
    "col-lg-push-5",
    "col-lg-push-6",
    "col-lg-push-7",
    "col-lg-push-8",
    "col-lg-push-9",
    "col-lg-push-10",
    "col-lg-push-11",

    "col-xs-pull-1",
    "col-xs-pull-2",
    "col-xs-pull-3",
    "col-xs-pull-4",
    "col-xs-pull-5",
    "col-xs-pull-6",
    "col-xs-pull-7",
    "col-xs-pull-8",
    "col-xs-pull-9",
    "col-xs-pull-10",
    "col-xs-pull-11",
    "col-sm-pull-1",
    "col-sm-pull-2",
    "col-sm-pull-3",
    "col-sm-pull-4",
    "col-sm-pull-5",
    "col-sm-pull-6",
    "col-sm-pull-7",
    "col-sm-pull-8",
    "col-sm-pull-9",
    "col-sm-pull-10",
    "col-sm-pull-11",
    "col-md-pull-1",
    "col-md-pull-2",
    "col-md-pull-3",
    "col-md-pull-4",
    "col-md-pull-5",
    "col-md-pull-6",
    "col-md-pull-7",
    "col-md-pull-8",
    "col-md-pull-9",
    "col-md-pull-10",
    "col-md-pull-11",
    "col-lg-pull-1",
    "col-lg-pull-2",
    "col-lg-pull-3",
    "col-lg-pull-4",
    "col-lg-pull-5",
    "col-lg-pull-6",
    "col-lg-pull-7",
    "col-lg-pull-8",
    "col-lg-pull-9",
    "col-lg-pull-10",
    "col-lg-pull-11",

    "col-xs-offset-1",
    "col-xs-offset-2",
    "col-xs-offset-3",
    "col-xs-offset-4",
    "col-xs-offset-5",
    "col-xs-offset-6",
    "col-xs-offset-7",
    "col-xs-offset-8",
    "col-xs-offset-9",
    "col-xs-offset-10",
    "col-xs-offset-11",
    "col-sm-offset-1",
    "col-sm-offset-2",
    "col-sm-offset-3",
    "col-sm-offset-4",
    "col-sm-offset-5",
    "col-sm-offset-6",
    "col-sm-offset-7",
    "col-sm-offset-8",
    "col-sm-offset-9",
    "col-sm-offset-10",
    "col-sm-offset-11",
    "col-md-offset-1",
    "col-md-offset-2",
    "col-md-offset-3",
    "col-md-offset-4",
    "col-md-offset-5",
    "col-md-offset-6",
    "col-md-offset-7",
    "col-md-offset-8",
    "col-md-offset-9",
    "col-md-offset-10",
    "col-md-offset-11",
    "col-lg-offset-1",
    "col-lg-offset-2",
    "col-lg-offset-3",
    "col-lg-offset-4",
    "col-lg-offset-5",
    "col-lg-offset-6",
    "col-lg-offset-7",
    "col-lg-offset-8",
    "col-lg-offset-9",
    "col-lg-offset-10",
    "col-lg-offset-11",

    "lead",

    "text-left",
    "text-center",
    "text-right",
    "text-muted",
    "text-primary",
    "text-success",
    "text-info",
    "text-warning",
    "text-danger",

    "list-unstyled",
    "list-inline",
    "dl-horizontal",

    "table",
    "table-striped",
    "table-bordered",
    "table-hover",
    "table-condensed",
    "table-responsive",
    "active",
    "success",
    "warning",
    "danger",

    "form",
    "form-group",
    "form-control",
    "form-inline",
    "form-horizontal",
    "control-label",
    "checkbox",
    "radio",
    "checkbox-inline",
    "radio-inline",
    "form-control-static",
    "has-warning",
    "has-error",
    "has-success",
    "help-block",
    "input-xs",
    "input-sm",
    "input-md",
    "input-lg",

    "btn",
    "btn-default",
    "btn-primary",
    "btn-success",
    "btn-info",
    "btn-warning",
    "btn-danger",
    "btn-link",
    "btn-xs",
    "btn-sm",
    "btn-md",
    "btn-lg",
    "btn-block",

    "img-rounded",
    "img-circle",
    "img-thumbnail",

    "close",
    "pull-left",
    "pull-right",
    "clearfix",
    "sr-only",
    "img-responsive",

    "visible-xs",
    "visible-sm",
    "visible-md",
    "visible-lg",
    "hidden-xs",
    "hidden-sm",
    "hidden-md",
    "hidden-lg",
    "visible-print",
    "hidden-print",

    "dropdown",
    "dropdown-menu",
    "dropdown-header",
    "dropdown-toggle",
    "divider",
    "disabled",

    "btn-group",
    "btn-group-xs",
    "btn-group-sm",
    "btn-group-md",
    "btn-group-lg",
    "btn-toolbar",
    "dropup",
    "caret",
    "btn-group-vertical",
    "btn-group-justified",

    "input-group",
    "input-group-addon",
    "input-group-btn",

    "nav",
    "nav-tabs",
    "nav-pills",
    "nav-stacked",
    "nav-justified",
    "navbar",
    "navbar-default",
    "navbar-header",
    "navbar-toggle",
    "navbar-brand",
    "navbar-nav",
    "navbar-form",
    "navbar-left",
    "navbar-right",
    "navbar-text",
    "navbar-link",
    "navbar-fixed-top",
    "navbar-fixed-bottom",
    "navbar-static-top",
    "navbar-inverse",
    "icon-bar",

    "breadcrumb",
    "pagination",
    "pagination-xs",
    "pagination-sm",
    "pagination-md",
    "pagination-lg",

    "pager",
    "previous",
    "next",

    "label",
    "label-default",
    "label-primary",
    "label-success",
    "label-info",
    "label-warning",
    "label-danger",

    "badge",

    "jumbotron",

    "page-header",
    "thumbnail",
    "caption",

    "alert",
    "alert-success",
    "alert-info",
    "alert-warning",
    "alert-danger",
    "alert-dismissable",
    "alert-link",

    "progress",
    "progress-striped",
    "progress-bar",
    "progress-bar-success",
    "progress-bar-info",
    "progress-bar-warning",
    "progress-bar-danger",

    "media",
    "media-object",
    "media-body",
    "media-heading",
    "media-list",

    "list-group",
    "list-group-item",
    "list-group-item-heading",
    "list-group-item-text",

    "panel",
    "panel-default",
    "panel-body",
    "panel-heading",
    "panel-title",
    "panel-footer",
    "panel-primary",
    "panel-success",
    "panel-info",
    "panel-warning",
    "panel-danger",

    "well",
    "well-xs",
    "well-sm",
    "well-md",
    "well-lg",

    "modal",
    "modal-dialog",
    "modal-title",
    "modal-content",
    "modal-header",
    "modal-footer",
    "modal-body",

    "tab-content",
    "tab-pane",

    "accordion-toggle",

    "collapse",
    "panel-collapse",
    "navbar-collapse",
    "navbar-ex1-collapse",

    "carousel",
    "carousel-indicators",
    "carousel-inner",
    "carousel-caption",
    "carousel-control",
    "left",
    "right",
    "icon-prev",
    "icon-next",
    "slide",

    "fade",
    "in",

    "glyphicon",
    "glyphicon-adjust",
    "glyphicon-align-center",
    "glyphicon-align-justify",
    "glyphicon-align-left",
    "glyphicon-align-right",
    "glyphicon-arrow-down",
    "glyphicon-arrow-left",
    "glyphicon-arrow-right",
    "glyphicon-arrow-up",
    "glyphicon-asterisk",
    "glyphicon-backward",
    "glyphicon-ban-circle",
    "glyphicon-barcode",
    "glyphicon-bell",
    "glyphicon-bold",
    "glyphicon-book",
    "glyphicon-bookmark",
    "glyphicon-briefcase",
    "glyphicon-bullhorn",
    "glyphicon-calendar",
    "glyphicon-camera",
    "glyphicon-certificate",
    "glyphicon-check",
    "glyphicon-chevron-down",
    "glyphicon-chevron-left",
    "glyphicon-chevron-right",
    "glyphicon-chevron-up",
    "glyphicon-circle-arrow-down",
    "glyphicon-circle-arrow-left",
    "glyphicon-circle-arrow-right",
    "glyphicon-circle-arrow-up",
    "glyphicon-cloud",
    "glyphicon-cloud-download",
    "glyphicon-cloud-upload",
    "glyphicon-cog",
    "glyphicon-collapse-down",
    "glyphicon-collapse-up",
    "glyphicon-comment",
    "glyphicon-compressed",
    "glyphicon-copyright-mark",
    "glyphicon-credit-card",
    "glyphicon-cutlery",
    "glyphicon-dashboard",
    "glyphicon-download",
    "glyphicon-download-alt",
    "glyphicon-earphone",
    "glyphicon-edit",
    "glyphicon-eject",
    "glyphicon-envelope",
    "glyphicon-euro",
    "glyphicon-exclamation-sign",
    "glyphicon-expand",
    "glyphicon-export",
    "glyphicon-eye-close",
    "glyphicon-eye-open",
    "glyphicon-facetime-video",
    "glyphicon-fast-backward",
    "glyphicon-fast-forward",
    "glyphicon-file",
    "glyphicon-film",
    "glyphicon-filter",
    "glyphicon-fire",
    "glyphicon-flag",
    "glyphicon-flash",
    "glyphicon-floppy-disk",
    "glyphicon-floppy-open",
    "glyphicon-floppy-remove",
    "glyphicon-floppy-save",
    "glyphicon-floppy-saved",
    "glyphicon-folder-close",
    "glyphicon-folder-open",
    "glyphicon-font",
    "glyphicon-forward",
    "glyphicon-fullscreen",
    "glyphicon-gbp",
    "glyphicon-gift",
    "glyphicon-glass",
    "glyphicon-globe",
    "glyphicon-hand-down",
    "glyphicon-hand-left",
    "glyphicon-hand-right",
    "glyphicon-hand-up",
    "glyphicon-hd-video",
    "glyphicon-hdd",
    "glyphicon-header",
    "glyphicon-headphones",
    "glyphicon-heart",
    "glyphicon-heart-empty",
    "glyphicon-home",
    "glyphicon-import",
    "glyphicon-inbox",
    "glyphicon-indent-left",
    "glyphicon-indent-right",
    "glyphicon-info-sign",
    "glyphicon-italic",
    "glyphicon-leaf",
    "glyphicon-link",
    "glyphicon-list",
    "glyphicon-list-alt",
    "glyphicon-lock",
    "glyphicon-log-in",
    "glyphicon-log-out",
    "glyphicon-magnet",
    "glyphicon-map-marker",
    "glyphicon-minus",
    "glyphicon-minus-sign",
    "glyphicon-move",
    "glyphicon-music",
    "glyphicon-new-window",
    "glyphicon-off",
    "glyphicon-ok",
    "glyphicon-ok-circle",
    "glyphicon-ok-sign",
    "glyphicon-open",
    "glyphicon-paperclip",
    "glyphicon-pause",
    "glyphicon-pencil",
    "glyphicon-phone",
    "glyphicon-phone-alt",
    "glyphicon-picture",
    "glyphicon-plane",
    "glyphicon-play",
    "glyphicon-play-circle",
    "glyphicon-plus",
    "glyphicon-plus-sign",
    "glyphicon-print",
    "glyphicon-pushpin",
    "glyphicon-qrcode",
    "glyphicon-question-sign",
    "glyphicon-random",
    "glyphicon-record",
    "glyphicon-refresh",
    "glyphicon-registration-mark",
    "glyphicon-remove",
    "glyphicon-remove-circle",
    "glyphicon-remove-sign",
    "glyphicon-repeat",
    "glyphicon-resize-full",
    "glyphicon-resize-horizontal",
    "glyphicon-resize-small",
    "glyphicon-resize-vertical",
    "glyphicon-retweet",
    "glyphicon-road",
    "glyphicon-save",
    "glyphicon-saved",
    "glyphicon-screenshot",
    "glyphicon-sd-video",
    "glyphicon-search",
    "glyphicon-send",
    "glyphicon-share",
    "glyphicon-share-alt",
    "glyphicon-shopping-cart",
    "glyphicon-signal",
    "glyphicon-sort",
    "glyphicon-sort-by-alphabet",
    "glyphicon-sort-by-alphabet-alt",
    "glyphicon-sort-by-attributes",
    "glyphicon-sort-by-attributes-alt",
    "glyphicon-sort-by-order",
    "glyphicon-sort-by-order-alt",
    "glyphicon-sound-5-1",
    "glyphicon-sound-6-1",
    "glyphicon-sound-7-1",
    "glyphicon-sound-dolby",
    "glyphicon-sound-stereo",
    "glyphicon-star",
    "glyphicon-star-empty",
    "glyphicon-stats",
    "glyphicon-step-backward",
    "glyphicon-step-forward",
    "glyphicon-stop",
    "glyphicon-subtitles",
    "glyphicon-tag",
    "glyphicon-tags",
    "glyphicon-tasks",
    "glyphicon-text-height",
    "glyphicon-text-width",
    "glyphicon-th",
    "glyphicon-th-large",
    "glyphicon-th-list",
    "glyphicon-thumbs-down",
    "glyphicon-thumbs-up",
    "glyphicon-time",
    "glyphicon-tint",
    "glyphicon-tower",
    "glyphicon-transfer",
    "glyphicon-trash",
    "glyphicon-tree-conifer",
    "glyphicon-tree-deciduous",
    "glyphicon-unchecked",
    "glyphicon-upload",
    "glyphicon-usd",
    "glyphicon-user",
    "glyphicon-volume-down",
    "glyphicon-volume-off",
    "glyphicon-volume-up",
    "glyphicon-warning-sign",
    "glyphicon-wrench",
    "glyphicon-zoom-in",
    "glyphicon-zoom-out"
]