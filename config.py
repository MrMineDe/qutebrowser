c = c
config = config

# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html
import subprocess
import os
import qutebrowser.api
from qutebrowser.api import interceptor

# Choose how to view certain data types
class viewer():
    media = "mpv"
    video = "mpv"
    audio = "mpv"
    image = "sxiv"
    pdf = "zathura"

# Editor settings
c.editor.command = [
    "nvim",
    "-f",
    "{file}",
    "-c",
    "normal {line}G{column0}1"
]
c.editor.encoding = "utf-8"

# Block youtube ads
def filter_yt(info: interceptor.Request):
    """Block given request if necessary"""
    url = info.request_url
    if (
        url.host() == "www.youtube.com"
        and url.path() == "/get_video_info"
        and "&adformat=" in url.query()
    ):
        info.block
interceptor.register(filter_yt)

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Set aliases
c.aliases = {
    "q": "close",# close current instance
    "qa": "quit",# close all instances
    "wqa": "quit --save",# save and close all instances
    "w": "session-save",
    "sd": "session-delete",
    "sl": "session-load",
    "so": "config-source",
    "h": "help",
    "H": "help -t",
}

# Auto save settings
c.auto_save.session = True
c.auto_save.interval = 15000

# Set default page
c.url.default_page = "https://search.brave.com/"

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`).  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {
    'DEFAULT': 'https://search.brave.com/search?q={}',
    # search github.com with the DEFAULT search engine
    '/sgh': 'https://search.brave.com/search?q=site%3Agithub.com {}',
    '/sgl': 'https://search.brave.com/search?q=site%3Agitlab.com {}',
    '/dn': 'https://www.britannica.com/dictionary/{}',
    '/od': 'https://odysee.com/$/search?q={}',
    '/yt': 'https://www.youtube.com/results?search_query={}',
    '/tw': 'https://www.twitch.tv/search?term={}',
    '/aw': 'https://wiki.archlinux.org/?search={}',
    '/aur': 'https://aur.archlinux.org/packages?={}',
    '/gh': 'https://github.com/NYANLAUNCHER?tab=repositories&q={}',
    '/lt': 'https://lutris.net/games?q={}',
    '/st': 'https://store.steampowered.com/search/?term={}',
    '/eu': 'https://wiki.eveuniversity.org/index.php?search={}',
}

# Set download settings
c.downloads.location.directory = "~/tmp/downloads"
c.downloads.remove_finished = 3 #seconds

# Set content settings
## set true for only the current window
c.content.autoplay = False

c.scrolling.bar = "when-searching"

# Set dark mode
## TODO: create blacklist to disable theme in certain webpages
blacklist = [ "https://discord.com/*", "https://www.youtube.com/*", "https://www.eveonline.com/*" ]

#config.set("colors.webpage.darkmode.enabled", True)

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', False, 'https://www.youtube.com')


# Keybinds
config.unbind("gC")
config.bind("gc", "tab-clone")
config.bind("gs", "open qute://settings")
config.bind("<Ctrl-q>", "close")
config.bind("<Ctrl-o>", "tab-focus last")
#config.bind("d", "")
#config.bind("d", "tab-close;; tab-focus last")
config.bind("<Ctrl-n>", "fake-key <Tab>")
config.bind("<Ctrl-p>", "fake-key <Shift-Tab>")
#view yt vid with viewer.video = "mpv"
config.bind(",v", "hint links spawn " + viewer.video + " {hint-url}")
config.bind(";v", "hint links spawn --detach " + viewer.video + " --force-window yes {hint-url}")
#hide tabs and cmdline
config.bind("xf", "config-cycle tabs.show always never;; config-cycle statusbar.show always never;; config-cycle scrolling.bar when-searching never")
config.bind("-", "zoom-out")
config.bind("=", "zoom-in")
config.bind("+", "zoom")
#config.bind("gM", "")# move a tab to <index> starting from the end
config.bind("<Ctrl-j>", "tab-move +")
config.bind("<Ctrl-k>", "tab-move -")

## Insert mode bindings
config.bind("<Ctrl-h>", "fake-key <Backspace>",          "insert")
config.bind("<Ctrl-a>", "fake-key <Home>",               "insert")
config.bind("<Ctrl-e>", "fake-key <End>",                "insert")
config.bind("<Ctrl-b>", "fake-key <Left>",               "insert")
config.bind("<Alt-b>",  "fake-key <Ctrl-Left>",          "insert")
config.bind("<Ctrl-f>", "fake-key <Right>",              "insert")
config.bind("<Alt-f>",  "fake-key <Ctrl-Right>",         "insert")
config.bind("<Ctrl-p>", "fake-key <Up>",                 "insert")
config.bind("<Ctrl-n>", "fake-key <Down>",               "insert")
config.bind("<Alt-d>",  "fake-key <Ctrl-Delete>",        "insert")
config.bind("<Ctrl-d>", "fake-key <Delete>",             "insert")
config.bind("<Ctrl-w>", "fake-key <Ctrl-backspace>",     "insert")
config.bind("<Ctrl-u>", "fake-key <Shift-Home><Delete>", "insert")
config.bind("<Ctrl-k>", "fake-key <Shift-End><Delete>",  "insert")

## Command mode bindings
config.unbind("<Ctrl-n>", "command")
config.unbind("<Ctrl-p>", "command")
config.bind("<Ctrl-n>", "fake-key <Tab>",       "command")
config.bind("<Ctrl-p>", "fake-key <Shift-Tab>", "command")
