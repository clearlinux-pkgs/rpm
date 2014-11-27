%global __os_install_post %{nil}

Name:           rpm
Version:        4.12.0.1
Release:        27
License:        LGPL-2.1
Summary:        The RPM package management system
Url:            http://rpm.org/
Group:          base
Source0:        http://rpm.org/releases/rpm-4.12.x/%{name}-%{version}.tar.bz2
Patch0:         0001-Explicitly-set-beecrypt-include-directory.patch
Patch1:         0002-Ensure-lib-is-used-and-not-lib64.patch
Patch2:         0003-debuginfo-do-not-strip-static-libraries.patch
Patch5:         0006-Fix-32bit-kernel-builds-by-not-using-eu-strip.patch
Patch6:         0007-scripts-Don-t-bail-out-when-debugedit-fails.patch
Patch7:         0001-fileattrs-Ensure-we-match-all-binaries-for-elf-depen.patch
Patch8:         0008-build-id-non-fatal.patch
Patch9:         ldconfig-posttrans.patch
Patch10:        minidebuginfo.patch
Patch11:	nopyo.patch

BuildRequires:  bzip2-dev
BuildRequires:  db-dev
BuildRequires:  elfutils-dev
BuildRequires:  file-dev
BuildRequires:  acl-dev
BuildRequires:  attr-dev
BuildRequires:  nss-dev nspr-dev
BuildRequires:  libstdc++-dev
BuildRequires:  openssl-dev
BuildRequires:  python-modules
BuildRequires:  xz-dev
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  popt-dev
BuildRequires:	gettext 
BuildRequires:  automake automake-dev
BuildRequires:  libtool-dev
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  libtool autoconf m4 gettext-dev autoconf pkg-config-dev
BuildRequires:	bison flex

%description
The RPM package management system.

%package -n rpm-doc
License:        LGPL-2.1
Summary:        The RPM package management system
Group:          doc

%description -n rpm-doc
The RPM package management system.

%package -n rpm-libs
License:        LGPL-2.1
Summary:        The RPM package management system
Group:          base

%description -n rpm-libs
The RPM package management system.

%package -n rpm-dev
License:        LGPL-2.1
Summary:        The RPM package management system
Group:          devel
Requires:       %{name} = %{version}
Requires:       bash
Requires:       rpm-libs

%description -n rpm-dev
The RPM package management system.

%package -n rpm-common
License:        LGPL-2.1
Summary:        The RPM package management system
Group:          base
Requires:       /bin/sh

%description -n rpm-common
The RPM package management system.

%package -n rpm-build
License:        LGPL-2.1
Summary:        Scripts and executable programs used to build packages
Group:          base
Requires:       %{name} = %{version}
Requires:       /bin/bash
Requires:       /bin/sh
Requires:       /usr/bin/perl
Requires:       cpio
Requires:       elfutils
Requires:       file-dev
Requires:       findutils
Requires:       rpm-libs = %{version}

%description -n rpm-build
The rpm-build packagec ontains the scripts and executable programs that are
used to build packages using the RPM Package Manager.

%package -n python-rpm-dev
License:        LGPL-2.1
Summary:        The RPM package management system
Group:          base

%description -n python-rpm-dev
The RPM Package Manager (RPM) is a powerful command line driven package
management system capable of installing, uninstalling, verifying, querying,
and updating software packages. Each software package consists of an
archive of files along with information about the package like its version,
a description, etc.

%package -n python-rpm
License:        LGPL-2.1
Summary:        Python bindings for apps which will manupulate RPM packages
Group:          base
Requires:       %{name} = %{version}
Requires:       rpm-libs = %{version}

%description -n python-rpm
The rpm-python package contains a module that permits applications written
in the Python programming language to use the interface supplied by the RPM
Package Manager libraries.

%package -n rpm-locale
License:        LGPL-2.1
Summary:        Translations for the rpm package
Group:          libs

%description -n rpm-locale
This package contains language translation files for rpm package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
# %patch10 -p1
%patch11 -p1


%build
autoreconf -fi
%configure --verbose \
 --sysconfdir=%{_sysconfdir} \
 --localstatedir=%{_localstatedir} \
 --with-file \
 --with-external-db \
 --with-path-magic=%{_usrlibrpm}/../../share/misc/magic.mgc \
 --with-syck=internal \
 --without-readline \
 --without-libtasn1 \
 --without-pakchois \
 --without-gnutls \
 --with-pcre \
 --enable-utf8 \
 --with-uuid \
 --with-attr \
 --with-acl \
 --with-popt=external \
 --with-pthreads \
 --without-cudf \
 --without-ficl \
 --without-aterm \
 --without-nix \
 --without-bash \
 --without-rc \
 --without-js \
 --without-gpsee \
 --without-ruby \
 --without-squirrel \
 --with-build-extlibdep \
 --with-build-maxextlibdep \
 --without-valgrind \
 --disable-openmp \
 --enable-build-pic \
 --enable-build-versionscript \
 --enable-build-warnings \
 --enable-build-debug \
 --enable-maintainer-mode \
 --with-path-macros=%{_usrlibrpm}/macros:%{_etcrpm}/macros.*:%{_etcrpm}/macros:%{_etcrpm}/%{_target}/macros \
 --with-path-lib=/usr/lib/rpm \
 --program-prefix= \
 --enable-nls \
 --without-augeas \
 --without-beecrypt \
 --without-internal-beecrypt \
 --with-bzip2 \
 --with-db \
 --with-dbsql \
 --without-db-tools-integrated \
 --without-gcrypt \
 --without-keyutils \
 --with-libelf \
 --without-lua \
 --without-neon \
 --without-libproxy \
 --without-expat \
 --without-gssapi \
 --without-nss \
 --with-openssl \
 --with-perl \
 --without-perl-urpm \
 --enable-python \
 --with-python=2.7 \
 --with-python-inc-dir=%{_includedir}/python2.7 \
 --with-python-lib-dir=%{_libdir}/python2.7/site-packages \
 --without-pythonembed \
 --without-selinux \
 --without-sepol \
 --without-semanage \
 --without-sqlite \
 --without-tcl \
 --without-xar \
 --enable-xz \
 --libdir=/usr/lib64 \
 --with-zlib \
 CPPFLAGS="-I/usr/include/nss3"

make %{?_smp_mflags}

%install
%make_install

# Make rpm accessible in usrbin
#mv %{buildroot}/bin/rpm %{buildroot}%{_bindir}/rpm
#rmdir %{buildroot}/bin

# Fix up symlinks that point to /bin/rpm
ln -sf rpm %{buildroot}%{_bindir}/rpmquery
ln -sf rpm %{buildroot}%{_bindir}/rpmverify

# this ensures perl doesnt go boom
rm %{buildroot}/usr/lib/rpm/fileattrs/perl.attr
rm %{buildroot}/usr/lib/rpm/fileattrs/perllib.attr

# since post-install hook is disabled on line1, replicate the
# behaviour of stripping libtool .la files
find %{buildroot} -name "*.la" -delete

%find_lang %{name}

%check
make check


%files
%{_bindir}/rpm
%{_bindir}/rpmdb
%{_bindir}/rpmgraph
%{_bindir}/rpmkeys
%{_bindir}/rpmquery
%{_bindir}/rpmsign
%{_bindir}/rpmspec
%{_bindir}/rpmverify
/usr/lib/rpm/macros
/usr/lib/rpm/rpm.daily
/usr/lib/rpm/rpm.log
/usr/lib/rpm/rpmpopt-*
/usr/lib/rpm/rpmrc
/usr/lib/rpm/tgpg
%{_libdir}/rpm-plugins/ldconfig.so

%files -n rpm-doc
%{_mandir}/*/man1/*
%{_mandir}/*/man8/*
%{_mandir}/man1/*
%{_mandir}/man8/*

%files -n rpm-libs
%{_libdir}/librpm.so.*
%{_libdir}/librpmbuild.so.*
%{_libdir}/librpmio.so.*
%{_libdir}/librpmsign.so.*

%files -n rpm-dev
%{_includedir}/rpm/*.h
%{_libdir}/librpm.so
%{_libdir}/librpmbuild.so
%{_libdir}/librpmio.so
%{_libdir}/librpmsign.so
%{_libdir}/pkgconfig/rpm.pc
/usr/lib/rpm/rpmdb_loadcvt

%files -n rpm-common
%{_bindir}/gendiff
%{_bindir}/rpm2cpio
%{_bindir}/rpm2archive

%files -n rpm-build
%{_bindir}/rpmbuild
%{_libdir}/rpm-plugins/syslog.so
/usr/lib/rpm/appdata.prov
/usr/lib/rpm/brp-*
/usr/lib/rpm/check-*
/usr/lib/rpm/config.guess
/usr/lib/rpm/config.sub
/usr/lib/rpm/debugedit
/usr/lib/rpm/desktop-file.prov
/usr/lib/rpm/elfdeps
/usr/lib/rpm/fileattrs/appdata.attr
/usr/lib/rpm/fileattrs/desktop.attr
/usr/lib/rpm/fileattrs/elf.attr
/usr/lib/rpm/fileattrs/font.attr
/usr/lib/rpm/fileattrs/libtool.attr
/usr/lib/rpm/fileattrs/mono.attr
/usr/lib/rpm/fileattrs/ocaml.attr
/usr/lib/rpm/fileattrs/pkgconfig.attr
/usr/lib/rpm/fileattrs/python.attr
/usr/lib/rpm/fileattrs/script.attr

# don't want these right now
# /usr/lib/rpm/fileattrs/perl.attr
# /usr/lib/rpm/fileattrs/perllib.attr

/usr/lib/rpm/find-debuginfo.sh
/usr/lib/rpm/find-lang.sh
/usr/lib/rpm/find-provides
/usr/lib/rpm/find-requires
/usr/lib/rpm/fontconfig.prov
/usr/lib/rpm/libtooldeps.sh
/usr/lib/rpm/macros.*
/usr/lib/rpm/mkinstalldirs
/usr/lib/rpm/mono-find-provides
/usr/lib/rpm/mono-find-requires
/usr/lib/rpm/ocaml-find-provides.sh
/usr/lib/rpm/ocaml-find-requires.sh
/usr/lib/rpm/osgideps.pl
/usr/lib/rpm/perl.prov
/usr/lib/rpm/perl.req
/usr/lib/rpm/perldeps.pl
/usr/lib/rpm/pkgconfigdeps.sh
/usr/lib/rpm/platform/*/macros
/usr/lib/rpm/pythondeps.sh
/usr/lib/rpm/rpm.supp
/usr/lib/rpm/rpm2cpio.sh
/usr/lib/rpm/rpmdeps
/usr/lib/rpm/script.req
/usr/lib/rpm/tcl.req

%files -n python-rpm-dev

%files -n python-rpm
/usr/lib/python2.7/site-packages/rpm/__init__.py
/usr/lib/python2.7/site-packages/rpm/_rpm.so
/usr/lib/python2.7/site-packages/rpm/_rpmb.so
/usr/lib/python2.7/site-packages/rpm/_rpms.so
/usr/lib/python2.7/site-packages/rpm/transaction.py

%files -n rpm-locale -f %{name}.lang