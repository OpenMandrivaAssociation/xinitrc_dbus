Summary:		Script check DBUS install for pcmanfm 0.9.8 and above
Name:			xinitrc_dbus
Version:		0.11.2
Release:		%mkrel 1
License:		GPLv2+
Group:			System/Base
Source0:		%{name}.sh
BuildArch:		noarch
Requires:		pcmanfm >= 0.9.8 dbus
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root

%description
This script add DBus entry to pcmanfm 0.9.8 and above

%prep

%build

%install
rm -rf %{buildroot}

mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
cp %SOURCE0  ${RPM_BUILD_ROOT}/%{_bindir}/xinitrc_dbus

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)

%{_bindir}/xinitrc_dbus
