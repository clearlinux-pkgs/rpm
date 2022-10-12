#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rpm
Version  : 4.17.0
Release  : 168
URL      : https://ftp.osuosl.org/pub/rpm/releases/rpm-4.17.x/rpm-4.17.0.tar.bz2
Source0  : https://ftp.osuosl.org/pub/rpm/releases/rpm-4.17.x/rpm-4.17.0.tar.bz2
Summary  : RPM Package Manager
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: rpm-bin = %{version}-%{release}
Requires: rpm-lib = %{version}-%{release}
Requires: rpm-license = %{version}-%{release}
Requires: rpm-locales = %{version}-%{release}
Requires: rpm-man = %{version}-%{release}
Requires: rpm-python = %{version}-%{release}
Requires: rpm-python3 = %{version}-%{release}
Requires: clr-rpm-config
Requires: debugedit
Requires: python-rpm-packaging
Requires: unzip
Requires: zip
BuildRequires : acl-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : bzip2-dev
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : file-dev
BuildRequires : gettext-bin
BuildRequires : gnupg
BuildRequires : libcap-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : lua-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgcrypt)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(nspr)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(zlib)
BuildRequires : popt-dev
BuildRequires : zstd-dev
Patch1: 0001-Ensure-lib-is-used-and-not-lib64.patch
Patch2: 0002-add-an-fflush.patch
Patch3: 0003-skip-pkgconfig-dep.patch
Patch4: 0004-Don-t-emit-compiler-version-requirement.patch
Patch5: 0005-fileattrs-Ensure-we-match-all-binaries-for-elf-depen.patch
Patch6: 0006-Add-ldconfig-post-transaction-hook.patch
Patch7: 0007-support-lib32-pkgconfig-files.patch
Patch8: 0008-preserve-timestamps.patch
Patch9: 0009-rpm-use-localhost-as-hostname-for-building-all-packa.patch
Patch10: 0010-fileattrs-Don-t-scan-libraries-in-glibc-auto-search-.patch
Patch11: 0011-Force-locale-files-not-to-be-executable.patch
Patch12: 0012-discover-uid0-based-on-usr-share-defaults.patch
Patch13: 0013-fix-debuginfo-build-id-matching-code.patch
Patch14: 0014-Remove-libtool-archive-symlinks-too.patch
Patch15: 0015-Avoid-printing-error-summary.patch
Patch16: delta-friendly-debuginfo.patch

%description
This is RPM, the RPM Package Manager.
The latest releases are always available at:

%package bin
Summary: bin components for the rpm package.
Group: Binaries
Requires: rpm-license = %{version}-%{release}

%description bin
bin components for the rpm package.


%package dev
Summary: dev components for the rpm package.
Group: Development
Requires: rpm-lib = %{version}-%{release}
Requires: rpm-bin = %{version}-%{release}
Provides: rpm-devel = %{version}-%{release}
Requires: rpm = %{version}-%{release}

%description dev
dev components for the rpm package.


%package extras
Summary: extras components for the rpm package.
Group: Default

%description extras
extras components for the rpm package.


%package lib
Summary: lib components for the rpm package.
Group: Libraries
Requires: rpm-license = %{version}-%{release}

%description lib
lib components for the rpm package.


%package license
Summary: license components for the rpm package.
Group: Default

%description license
license components for the rpm package.


%package locales
Summary: locales components for the rpm package.
Group: Default

%description locales
locales components for the rpm package.


%package man
Summary: man components for the rpm package.
Group: Default

%description man
man components for the rpm package.


%package python
Summary: python components for the rpm package.
Group: Default
Requires: rpm-python3 = %{version}-%{release}

%description python
python components for the rpm package.


%package python3
Summary: python3 components for the rpm package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rpm package.


%prep
%setup -q -n rpm-4.17.0
cd %{_builddir}/rpm-4.17.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665600173
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%reconfigure --disable-static --disable-werror \
--disable-openmp \
--enable-zstd \
--disable-bdb \
--enable-sqlite \
--disable-rpath \
--enable-python \
--disable-inhibit-plugin \
--with-crypto=libgcrypt \
--with-archive \
--without-selinux \
--without-imaevm \
--with-cap \
--with-acl \
--with-lua \
--without-audit
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1665600173
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rpm
cp %{_builddir}/rpm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/rpm/588760a9f446cebfc4b61485cd09cd768908337f || :
%make_install
%find_lang rpm
## Remove excluded files
rm -f %{buildroot}*/usr/lib/rpm/fileattrs/perl.attr
rm -f %{buildroot}*/usr/lib/rpm/fileattrs/perllib.attr

%files
%defattr(-,root,root,-)
/usr/lib/rpm/brp-compress
/usr/lib/rpm/brp-elfperms
/usr/lib/rpm/brp-remove-la-files
/usr/lib/rpm/brp-strip
/usr/lib/rpm/brp-strip-comment-note
/usr/lib/rpm/brp-strip-static-archive
/usr/lib/rpm/check-buildroot
/usr/lib/rpm/check-files
/usr/lib/rpm/check-prereqs
/usr/lib/rpm/check-rpaths
/usr/lib/rpm/check-rpaths-worker
/usr/lib/rpm/elfdeps
/usr/lib/rpm/fileattrs/debuginfo.attr
/usr/lib/rpm/fileattrs/desktop.attr
/usr/lib/rpm/fileattrs/elf.attr
/usr/lib/rpm/fileattrs/font.attr
/usr/lib/rpm/fileattrs/metainfo.attr
/usr/lib/rpm/fileattrs/ocaml.attr
/usr/lib/rpm/fileattrs/pkgconfig.attr
/usr/lib/rpm/fileattrs/script.attr
/usr/lib/rpm/find-lang.sh
/usr/lib/rpm/find-provides
/usr/lib/rpm/find-requires
/usr/lib/rpm/fontconfig.prov
/usr/lib/rpm/macros
/usr/lib/rpm/mkinstalldirs
/usr/lib/rpm/ocamldeps.sh
/usr/lib/rpm/perl.prov
/usr/lib/rpm/perl.req
/usr/lib/rpm/pkgconfigdeps.sh
/usr/lib/rpm/platform/aarch64-linux/macros
/usr/lib/rpm/platform/alpha-linux/macros
/usr/lib/rpm/platform/alphaev5-linux/macros
/usr/lib/rpm/platform/alphaev56-linux/macros
/usr/lib/rpm/platform/alphaev6-linux/macros
/usr/lib/rpm/platform/alphaev67-linux/macros
/usr/lib/rpm/platform/alphapca56-linux/macros
/usr/lib/rpm/platform/amd64-linux/macros
/usr/lib/rpm/platform/armv3l-linux/macros
/usr/lib/rpm/platform/armv4b-linux/macros
/usr/lib/rpm/platform/armv4l-linux/macros
/usr/lib/rpm/platform/armv5tejl-linux/macros
/usr/lib/rpm/platform/armv5tel-linux/macros
/usr/lib/rpm/platform/armv5tl-linux/macros
/usr/lib/rpm/platform/armv6hl-linux/macros
/usr/lib/rpm/platform/armv6l-linux/macros
/usr/lib/rpm/platform/armv7hl-linux/macros
/usr/lib/rpm/platform/armv7hnl-linux/macros
/usr/lib/rpm/platform/armv7l-linux/macros
/usr/lib/rpm/platform/armv8hl-linux/macros
/usr/lib/rpm/platform/armv8l-linux/macros
/usr/lib/rpm/platform/athlon-linux/macros
/usr/lib/rpm/platform/geode-linux/macros
/usr/lib/rpm/platform/i386-linux/macros
/usr/lib/rpm/platform/i486-linux/macros
/usr/lib/rpm/platform/i586-linux/macros
/usr/lib/rpm/platform/i686-linux/macros
/usr/lib/rpm/platform/ia32e-linux/macros
/usr/lib/rpm/platform/ia64-linux/macros
/usr/lib/rpm/platform/m68k-linux/macros
/usr/lib/rpm/platform/mips-linux/macros
/usr/lib/rpm/platform/mips64-linux/macros
/usr/lib/rpm/platform/mips64el-linux/macros
/usr/lib/rpm/platform/mips64r6-linux/macros
/usr/lib/rpm/platform/mips64r6el-linux/macros
/usr/lib/rpm/platform/mipsel-linux/macros
/usr/lib/rpm/platform/mipsr6-linux/macros
/usr/lib/rpm/platform/mipsr6el-linux/macros
/usr/lib/rpm/platform/noarch-linux/macros
/usr/lib/rpm/platform/pentium3-linux/macros
/usr/lib/rpm/platform/pentium4-linux/macros
/usr/lib/rpm/platform/ppc-linux/macros
/usr/lib/rpm/platform/ppc32dy4-linux/macros
/usr/lib/rpm/platform/ppc64-linux/macros
/usr/lib/rpm/platform/ppc64iseries-linux/macros
/usr/lib/rpm/platform/ppc64le-linux/macros
/usr/lib/rpm/platform/ppc64p7-linux/macros
/usr/lib/rpm/platform/ppc64pseries-linux/macros
/usr/lib/rpm/platform/ppc8260-linux/macros
/usr/lib/rpm/platform/ppc8560-linux/macros
/usr/lib/rpm/platform/ppciseries-linux/macros
/usr/lib/rpm/platform/ppcpseries-linux/macros
/usr/lib/rpm/platform/riscv64-linux/macros
/usr/lib/rpm/platform/s390-linux/macros
/usr/lib/rpm/platform/s390x-linux/macros
/usr/lib/rpm/platform/sh-linux/macros
/usr/lib/rpm/platform/sh3-linux/macros
/usr/lib/rpm/platform/sh4-linux/macros
/usr/lib/rpm/platform/sh4a-linux/macros
/usr/lib/rpm/platform/sparc-linux/macros
/usr/lib/rpm/platform/sparc64-linux/macros
/usr/lib/rpm/platform/sparc64v-linux/macros
/usr/lib/rpm/platform/sparcv8-linux/macros
/usr/lib/rpm/platform/sparcv9-linux/macros
/usr/lib/rpm/platform/sparcv9v-linux/macros
/usr/lib/rpm/platform/x86_64-linux/macros
/usr/lib/rpm/rpm.daily
/usr/lib/rpm/rpm.log
/usr/lib/rpm/rpm.supp
/usr/lib/rpm/rpm2cpio.sh
/usr/lib/rpm/rpmdb_dump
/usr/lib/rpm/rpmdb_load
/usr/lib/rpm/rpmdeps
/usr/lib/rpm/rpmpopt-4.17.0
/usr/lib/rpm/rpmrc
/usr/lib/rpm/script.req
/usr/lib/rpm/tgpg

%files bin
%defattr(-,root,root,-)
/usr/bin/gendiff
/usr/bin/rpm
/usr/bin/rpm2archive
/usr/bin/rpmbuild
/usr/bin/rpmdb
/usr/bin/rpmgraph
/usr/bin/rpmkeys
/usr/bin/rpmquery
/usr/bin/rpmsign
/usr/bin/rpmspec
/usr/bin/rpmverify

%files dev
%defattr(-,root,root,-)
/usr/include/rpm/argv.h
/usr/include/rpm/header.h
/usr/include/rpm/rpmarchive.h
/usr/include/rpm/rpmbase64.h
/usr/include/rpm/rpmbuild.h
/usr/include/rpm/rpmcallback.h
/usr/include/rpm/rpmcli.h
/usr/include/rpm/rpmdb.h
/usr/include/rpm/rpmds.h
/usr/include/rpm/rpmfc.h
/usr/include/rpm/rpmfi.h
/usr/include/rpm/rpmfiles.h
/usr/include/rpm/rpmfileutil.h
/usr/include/rpm/rpmio.h
/usr/include/rpm/rpmkeyring.h
/usr/include/rpm/rpmlib.h
/usr/include/rpm/rpmlog.h
/usr/include/rpm/rpmmacro.h
/usr/include/rpm/rpmpgp.h
/usr/include/rpm/rpmpol.h
/usr/include/rpm/rpmprob.h
/usr/include/rpm/rpmps.h
/usr/include/rpm/rpmsign.h
/usr/include/rpm/rpmspec.h
/usr/include/rpm/rpmsq.h
/usr/include/rpm/rpmstring.h
/usr/include/rpm/rpmstrpool.h
/usr/include/rpm/rpmsw.h
/usr/include/rpm/rpmtag.h
/usr/include/rpm/rpmtd.h
/usr/include/rpm/rpmte.h
/usr/include/rpm/rpmts.h
/usr/include/rpm/rpmtypes.h
/usr/include/rpm/rpmurl.h
/usr/include/rpm/rpmutil.h
/usr/include/rpm/rpmver.h
/usr/lib64/librpm.so
/usr/lib64/librpmbuild.so
/usr/lib64/librpmio.so
/usr/lib64/librpmsign.so
/usr/lib64/pkgconfig/rpm.pc

%files extras
%defattr(-,root,root,-)
/usr/bin/rpm2cpio

%files lib
%defattr(-,root,root,-)
/usr/lib64/librpm.so.9
/usr/lib64/librpm.so.9.2.0
/usr/lib64/librpmbuild.so.9
/usr/lib64/librpmbuild.so.9.2.0
/usr/lib64/librpmio.so.9
/usr/lib64/librpmio.so.9.2.0
/usr/lib64/librpmsign.so.9
/usr/lib64/librpmsign.so.9.2.0
/usr/lib64/rpm-plugins/fsverity.so
/usr/lib64/rpm-plugins/ima.so
/usr/lib64/rpm-plugins/ldconfig.so
/usr/lib64/rpm-plugins/prioreset.so
/usr/lib64/rpm-plugins/syslog.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rpm/588760a9f446cebfc4b61485cd09cd768908337f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/fr/man8/rpm.8
/usr/share/man/ja/man8/rpm.8
/usr/share/man/ja/man8/rpm2cpio.8
/usr/share/man/ja/man8/rpmbuild.8
/usr/share/man/ja/man8/rpmgraph.8
/usr/share/man/ko/man8/rpm.8
/usr/share/man/ko/man8/rpm2cpio.8
/usr/share/man/man1/gendiff.1
/usr/share/man/man8/rpm-misc.8
/usr/share/man/man8/rpm-plugin-ima.8
/usr/share/man/man8/rpm-plugin-prioreset.8
/usr/share/man/man8/rpm-plugin-syslog.8
/usr/share/man/man8/rpm-plugins.8
/usr/share/man/man8/rpm.8
/usr/share/man/man8/rpm2archive.8
/usr/share/man/man8/rpm2cpio.8
/usr/share/man/man8/rpmbuild.8
/usr/share/man/man8/rpmdb.8
/usr/share/man/man8/rpmdeps.8
/usr/share/man/man8/rpmgraph.8
/usr/share/man/man8/rpmkeys.8
/usr/share/man/man8/rpmsign.8
/usr/share/man/man8/rpmspec.8
/usr/share/man/pl/man1/gendiff.1
/usr/share/man/pl/man8/rpm.8
/usr/share/man/pl/man8/rpm2cpio.8
/usr/share/man/pl/man8/rpmbuild.8
/usr/share/man/pl/man8/rpmdeps.8
/usr/share/man/pl/man8/rpmgraph.8
/usr/share/man/ru/man8/rpm.8
/usr/share/man/ru/man8/rpm2cpio.8
/usr/share/man/sk/man8/rpm.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f rpm.lang
%defattr(-,root,root,-)

