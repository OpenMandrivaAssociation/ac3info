%define name ac3info
%define version 0.1
%define release %mkrel 4

Summary: A tool to display ac3 properties
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: File tools
Url: http://konilope.linuxeries.org/ac3info/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This tool display some informations about some ac3 files

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/ac3info

%changelog
