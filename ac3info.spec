%define debug_package	%{nil}

Summary: A tool to display ac3 properties
Name: ac3info
Version: 0.1
Release: 7
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: File tools
Url: http://konilope.linuxeries.org/ac3info/

%description
This tool display some informations about some ac3 files

%prep
%setup -q

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/ac3info
