pkgname = "kdeplasma-addons"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
# FIXME: failed tz comparison / scientific notation number e uppercase
make_check_args = ["-E", "(converterrunnertest|datetimerunnertest)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdeclarative-devel",
    "kglobalaccel-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kjobwidgets-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "krunner-devel",
    "kservice-devel",
    "kunitconversion-devel",
    "kxmlgui-devel",
    "libplasma-devel",
    "plasma5support-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtquick3d-devel",
    "sonnet-devel",
]
depends = [
    "kirigami-addons",
    "kitemmodels",
    "purpose",
    "qt6-qtquick3d",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Plasma addons"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-only AND CC0-1.0 AND LGPL-3.0-or-later"
url = "https://invent.kde.org/plasma/kdeplasma-addons"
source = f"$(KDE_SITE)/plasma/{pkgver}/kdeplasma-addons-{pkgver}.tar.xz"
sha256 = "911af4754873c17c1ca7d49f0669de3e386858b09adf282783b9c5510576ba95"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]


@subpackage("kdeplasma-addons-devel")
def _devel(self):
    return self.default_devel()
