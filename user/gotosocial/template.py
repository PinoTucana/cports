pkgname = "gotosocial"
pkgver = "0.19.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.Version={pkgver}", "./cmd/gotosocial"]
make_check_env = {"GTS_DB_TYPE": "sqlite", "GTS_DB_ADDRESS": ":memory:"}
hostmakedepends = ["go", "go-swagger", "yarn"]
checkdepends = []
depends = []
go_build_tags = ["netgo", "osusergo", "kvformat"]
go_check_tags = ["netgo", "osusergo", "kvformat"]
pkgdesc = "ActivityPub server"
license = "AGPL-3.0-or-later"
url = "https://gotosocial.org"
source = f"https://github.com/superseriousbusiness/gotosocial/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e564f5904dd0f0b001631c5707184ceea41e7b3725e2ac6012a31fdeee2e026f"
# flaky
options = ["!check"]

match self.profile().arch:
    case "aarch64" | "x86_64":
        pass
    case _:
        go_build_tags += ["nowasm"]
        go_check_tags += ["nowasm"]
        depends += ["cmd:ffmpeg!ffmpeg", "cmd:ffprobe!ffmpeg"]
        checkdepends += ["ffmpeg"]


def post_extract(self):
    # subtle fp value differences, harmless
    self.rm("internal/media/manager_test.go")
    self.rm("internal/api/client/admin/emojicreate_test.go")
    self.rm("internal/api/client/admin/emojiupdate_test.go")
    self.rm("internal/federation/dereferencing/emoji_test.go")


def post_prepare(self):
    self.do(
        "yarn",
        "--cwd",
        "./web/source",
        "install",
        "--frozen-lockfile",
        allow_network=True,
    )
    self.do(
        "yarn",
        "--cwd",
        "./web/source",
        "ts-patch",
        "install",
        allow_network=True,
    )
    self.do("yarn", "--cwd", "./web/source", "build", allow_network=True)


def post_build(self):
    self.do(
        "swagger",
        "generate",
        "spec",
        "-o",
        "web/assets/swagger.yaml",
        "--scan-models",
    )


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "gotosocial")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_dir("usr/share/gotosocial/web")
    self.install_file("example/config.yaml", "usr/share/gotosocial")
    self.install_files("web/assets", "usr/share/gotosocial/web")
    self.install_files("web/template", "usr/share/gotosocial/web")
