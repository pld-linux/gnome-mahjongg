# TODO: switch to gtk4-update-icon-cache
Summary:	GNOME Mahjongg
Summary(pl.UTF-8):	Mahjongg dla GNOME
Name:		gnome-mahjongg
Version:	3.40.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-mahjongg/3.40/%{name}-%{version}.tar.xz
# Source0-md5:	31027da9916f983237083e819bbbc4b4
URL:		https://wiki.gnome.org/Apps/Mahjongg
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk4-devel >= 4.5.0
BuildRequires:	libadwaita-devel >= 1
BuildRequires:	librsvg-devel >= 1:2.46.0
BuildRequires:	meson >= 0.57.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-librsvg >= 1:2.46.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk4 >= 4.5.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%{_datadir}/gnome-mahjongg
%{_datadir}/metainfo/org.gnome.Mahjongg.appdata.xml
%{_desktopdir}/org.gnome.Mahjongg.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Mahjongg.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Mahjongg-symbolic.svg
%{_mandir}/man6/gnome-mahjongg.6*
