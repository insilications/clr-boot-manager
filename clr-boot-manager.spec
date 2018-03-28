#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x646B4C3749D208F2 (william.r.douglas@gmail.com)
#
Name     : clr-boot-manager
Version  : 2.0.0
Release  : 27
URL      : https://github.com/clearlinux/clr-boot-manager/releases/download/v2.0.0/clr-boot-manager-2.0.0.tar.xz
Source0  : https://github.com/clearlinux/clr-boot-manager/releases/download/v2.0.0/clr-boot-manager-2.0.0.tar.xz
Source1  : clr-boot-manager-motd.service
Source99 : https://github.com/clearlinux/clr-boot-manager/releases/download/v2.0.0/clr-boot-manager-2.0.0.tar.xz.asc
Summary  : Common C library functions
Group    : Development/Tools
License  : LGPL-2.1
Requires: clr-boot-manager-bin
Requires: clr-boot-manager-config
Requires: clr-boot-manager-autostart
Requires: clr-boot-manager-doc
BuildRequires : efivar-dev
BuildRequires : gnu-efi-dev
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(systemd)
BuildRequires : python3
BuildRequires : systemd-boot
BuildRequires : valgrind
Patch1: 0001-Ease-performance-impact-of-kernel-booted-detection.patch
Patch2: 0002-Remove-file-descriptor-leak-check.patch
Patch3: 0003-Add-documentation-to-man-page-for-kernel-configurati.patch
Patch4: 0004-Motd-update-script-for-cbm.patch
Patch5: 0005-bootman-use-one-initrd-on-Clear-Linux.patch

%description
clr-boot-manager
----------------
[![Build Status](https://travis-ci.org/clearlinux/clr-boot-manager.svg?branch=master)](https://travis-ci.org/clearlinux/clr-boot-manager)

%package autostart
Summary: autostart components for the clr-boot-manager package.
Group: Default

%description autostart
autostart components for the clr-boot-manager package.


%package bin
Summary: bin components for the clr-boot-manager package.
Group: Binaries
Requires: clr-boot-manager-config

%description bin
bin components for the clr-boot-manager package.


%package config
Summary: config components for the clr-boot-manager package.
Group: Default

%description config
config components for the clr-boot-manager package.


%package doc
Summary: doc components for the clr-boot-manager package.
Group: Documentation

%description doc
doc components for the clr-boot-manager package.


%prep
%setup -q -n clr-boot-manager-2.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522260275
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dwith-vendor-prefix=Clear-linux \
-Dwith-kernel-modules-dir=/usr/lib/modules \
-Dwith-kernel-namespace=org.clearlinux \
-Dwith-bootloader=shim-systemd-boot builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/clr-boot-manager-motd.service
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../clr-boot-manager-booted.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service
mkdir -p %{buildroot}/usr/bin
install -m0755 clr-boot-manager-motd.sh %{buildroot}/usr/bin/clr-boot-manager-motd.sh
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -sf ../clr-boot-manager-motd.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/clr-boot-manager-motd.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-boot-manager
/usr/bin/clr-boot-manager-motd.sh

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service
/usr/lib/systemd/system/clr-boot-manager-booted.service
/usr/lib/systemd/system/clr-boot-manager-motd.service
/usr/lib/systemd/system/update-triggers.target.wants/clr-boot-manager-motd.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
