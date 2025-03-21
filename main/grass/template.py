pkgname = "grass"
pkgver = "0.13.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Sass compiler"
license = "MIT"
url = "https://github.com/connorskees/grass"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "577858cce48440d161c6036d83dbfb3c173058f9df297977b13b8646f88a4906"


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/grass")
    self.install_license("LICENSE")
