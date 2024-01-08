Summary: Connman plugin for GNetworkMonitor
Name: connman-network-monitor
Version: 0.0.0
Release: 1
License: LGPLv2
URL:     https://github.com/sailfishos/connman-network-monitor
Source0: %{name}-%{version}.tar.bz2
Patch0:  Fix-deprecation-errors-from-glib.patch
Patch1:  Fix-makefile.patch
Patch2:  Add-dummy-network-metered-property.patch
Patch3:  Delay-changes-to-ready-state.patch
BuildRequires: automake, autoconf, libtool
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
Requires:      connman

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream
./autogen.sh

%build
%configure

%make_build

%install
%make_install

find %{buildroot} -name \*.a -delete

%files
%{_libdir}/gio/modules/lib%{name}.so
