Name: meego-netbook-backgrounds
Summary: MeeGo netbook desktop backgrounds
Version: 0.6
Release: %mkrel 1
License: LGPLv2
Group: Applications/Multimedia
Source0: netbook-backgrounds-%{version}.tar.bz2
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Desktop wallpaper artwork.

%prep
%setup -q -n netbook-backgrounds-%{version}

%build

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root,-)
%{_datadir}/plymouth/shutdown-1024x600.png
%{_datadir}/plymouth/shutdown-1366x768.png
%{_datadir}/plymouth/splash.png
%{_datadir}/backgrounds/images/meego-background.png
%{_datadir}/backgrounds/images/myzone-default-background.png
