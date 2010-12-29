%define distsuffix edm

Summary:        Script check DBUS install for pcmanfm 0.9.7
Name:           xinitrc_dbus
Version:        0.11.2
Release:        %mkrel 1
License:        GPLv2+
Group:          System Environment/Base
Source0:        %{name}.sh
BuildArch:      noarch
Requires:	pcmanfm dbus

%description
This script add DBus entry to pcmanfm 0.9.7

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
cp %SOURCE0  ${RPM_BUILD_ROOT}/%{_bindir}/xinitrc_dbus

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)

%{_bindir}/xinitrc_dbus

