pkgname = "firmware-sof"
pkgver = "2023.09"
pkgrel = 0
archs = ["x86_64"]
install_if = [f"base-firmware-sof={pkgver}-r{pkgrel}"]
pkgdesc = "Sound Open Firmware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-{pkgver}.tar.gz"
sha256 = "4bcc75c6642348e1a516db7ff9d050b6ea1b8672983542c6952562fa8c1c7b63"
options = ["!strip", "foreignelf"]


def do_install(self):
    for folder in ["sof", "sof-ace-tplg", "sof-ipc4", "sof-tplg"]:
        self.install_files(
            folder, "usr/lib/firmware/intel", name=f"{folder}-v{pkgver}"
        )
        self.install_link(
            f"{folder}-v{pkgver}", f"usr/lib/firmware/intel/{folder}"
        )
    self.install_license("LICENCE.NXP")
    self.install_license("LICENCE.Intel")


@subpackage("base-firmware-sof")
def _base(self):
    self.pkgdesc = f"{pkgdesc} (base metapackage)"
    self.build_style = "meta"

    return []
