Name:           whatsapp-for-linux
Version:        1.0.7
Release:        1
Summary:        An unofficial WhatsApp linux client written in C++ with the help of gtkmm-3.0 and webkit2.
License:        GPLv3.0
URL:            https://github.com/eneshecan/whatsapp-for-linux
Source0:        https://github.com/eneshecan/whatsapp-for-linux/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtkmm-3.0)


%description
Whatsapp-for-linux is an unofficial WhatsApp linux client written in C++ with the help of gtkmm-3.0 and webkit2.
 
%prep
%autosetup -p1 -n %{name}-%{version}
 
%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release

%make_build

%install
%make_install -C build

%files
%{_bindir}/whatsapp-for-linux
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
