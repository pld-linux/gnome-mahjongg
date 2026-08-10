# TODO: switch to gtk4-update-icon-cache
Summary:	GNOME Mahjongg
Summary(pl.UTF-8):	Mahjongg dla GNOME
Name:		gnome-mahjongg
Version:	49.1.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-mahjongg/49/%{name}-%{version}.tar.xz
# Source0-md5:	2f80ef2b1caeb0f64bbd7cea204787b4
URL:		https://apps.gnome.org/Mahjongg/
BuildRequires:	AppStream
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	gtk4-devel >= 4.20.0
BuildRequires:	libadwaita-devel >= 1.8
BuildRequires:	librsvg-devel >= 1:2.46.0
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-libadwaita >= 1.8
BuildRequires:	vala-librsvg >= 1:2.46.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.72.0
Requires:	glib2 >= 1:2.72.0
Requires:	gtk4 >= 4.20.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.8
Requires:	librsvg >= 1:2.46.0
Provides:	gnome-games-mahjongg = 1:%{version}-%{release}
Obsoletes:	gnome-games-mahjongg < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disassemble a pile of tiles by removing matching pairs.

%description -l pl.UTF-8
Gra polegająca na demontażu stosu kafli poprzez usuwanie pasujących
par.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-mahjongg
%{_datadir}/dbus-1/services/org.gnome.Mahjongg.service
%{_datadir}/glib-2.0/schemas/org.gnome.Mahjongg.gschema.xml
%{_datadir}/metainfo/org.gnome.Mahjongg.metainfo.xml
%{_desktopdir}/org.gnome.Mahjongg.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Mahjongg.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Mahjongg-symbolic.svg
%{_mandir}/man6/gnome-mahjongg.6*
