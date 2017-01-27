Summary:	GNOME Mahjongg
Summary(pl.UTF-8):	Mahjongg dla GNOME
Name:		gnome-mahjongg
Version:	3.22.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-mahjongg/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	8493c4601d938dcbaa10b56b4a301486
URL:		https://wiki.gnome.org/Apps/Mahjongg
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.13.2
BuildRequires:	intltool >= 0.50.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.13.2
Requires:	hicolor-icon-theme
Requires:	librsvg >= 2.32.0
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-mahjongg
%{_datadir}/appdata/gnome-mahjongg.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mahjongg.gschema.xml
%{_datadir}/gnome-mahjongg
%{_desktopdir}/gnome-mahjongg.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-mahjongg.png
%{_iconsdir}/hicolor/scalable/apps/gnome-mahjongg.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-mahjongg-symbolic.svg
%{_mandir}/man6/gnome-mahjongg.6*
