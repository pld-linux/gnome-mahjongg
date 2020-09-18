Summary:	GNOME Mahjongg
Summary(pl.UTF-8):	Mahjongg dla GNOME
Name:		gnome-mahjongg
Version:	3.38.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-mahjongg/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	4ee6ffd8bbaabef0aaf42b717c35a614
URL:		https://wiki.gnome.org/Apps/Mahjongg
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.13.2
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.13.2
Requires:	hicolor-icon-theme
Requires:	librsvg >= 1:2.32.0
Provides:	gnome-games-mahjongg
Provides:	gnome-games-mahjongg = 1:%{version}-%{release}
Obsoletes:	gnome-games-mahjongg
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
%{_datadir}/glib-2.0/schemas/org.gnome.Mahjongg.gschema.xml
%{_datadir}/gnome-mahjongg
%{_datadir}/metainfo/org.gnome.Mahjongg.appdata.xml
%{_desktopdir}/org.gnome.Mahjongg.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Mahjongg.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Mahjongg-symbolic.svg
%{_mandir}/man6/gnome-mahjongg.6*
