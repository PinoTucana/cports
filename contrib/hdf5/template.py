pkgname = "hdf5"
pkgver = "1.14.4.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DHDF5_BUILD_CPP_LIB=ON",
    "-DHDF5_BUILD_EXAMPLES=OFF",
    "-DHDF5_BUILD_FORTRAN=OFF",
    "-DHDF5_BUILD_HL_LIB=OFF",  # also fortran
    "-DHDF5_BUILD_STATIC_TOOLS=OFF",
    "-DHDF5_INSTALL_DOC_DIR=share/doc/hdf5",
    "-DHDF5_INSTALL_CMAKE_DIR=lib/cmake",
    "-DHDF5_BUILD_TOOLS=ON",
    "-DHDF5_ENABLE_SZIP_ENCODING=ON",
    "-DHDF5_ENABLE_SZIP_SUPPORT=ON",
    "-DHDF5_ENABLE_Z_LIB_SUPPORT=ON",
    "-Dlibaec_DIR=/usr/lib/cmake",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "libaec-devel",
    "zlib-devel",
]
pkgdesc = "HDF5 data model library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause AND BSD-3-Clause-LBNL"
url = "https://www.hdfgroup.org/solutions/hdf5"
# last . is - in the source tarballs
source = f"https://github.com/HDFGroup/hdf5/releases/download/hdf5_{pkgver}/hdf5-{'-'.join(pkgver.rsplit('.', 1))}.tar.gz"
sha256 = "019ac451d9e1cf89c0482ba2a06f07a46166caf23f60fea5ef3c37724a318e03"
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING_LBNL_HDF5")


@subpackage("hdf5-devel")
def _devel(self):
    return self.default_devel()


@subpackage("hdf5-progs")
def _progs(self):
    return self.default_progs()
