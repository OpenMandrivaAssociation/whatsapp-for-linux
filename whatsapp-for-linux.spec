Name:           whatsapp-for-linux
Version:        1.7.0
Release:        1
Summary:        An unofficial WhatsApp linux client written in C++ with the help of gtkmm-3.0 and webkit2.
Group:          Networking/Instant messaging
License:        GPLv3.0
URL:            https://github.com/eneshecan/whatsapp-for-linux
Source0:        https://github.com/eneshecan/whatsapp-for-linux/archive/v%{version}/WasIstLos-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: pkgconfig(gtkmm-3.0)

%rename WasIstLos

%description
Whatsapp-for-linux is an unofficial WhatsApp linux client written in C++ with the help of gtkmm-3.0 and webkit2.
 
%prep
%autosetup -p1 -n WasIstLos-%{version}
 
%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release

%make_build

%install
%make_install -C build

%find_lang wasistlos

%files -f wasistlos.lang
%{_bindir}/wasistlos
%{_datadir}/applications/com.github.xeco23.WasIstLos.desktop
%{_iconsdir}/hicolor/*x*/apps/com.github.xeco23.WasIstLos.png
%{_iconsdir}/hicolor/*x*/status/com.github.xeco23.WasIstLos-*
%{_datadir}/metainfo/com.github.xeco23.WasIstLos.appdata.xml
