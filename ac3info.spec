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
%defattr(-,root,root)
%{_bindir}/ac3info



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdv2011.0
+ Revision: 616496
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2010.0
+ Revision: 423932
- rebuild

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2010.0
+ Revision: 423858
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.1-2mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Funda Wang <fwang@mandriva.org> 0.1-2mdv2008.0
+ Revision: 25000
- fix rpm group

* Mon May 07 2007 Erwan Velu <erwan@mandriva.org> 0.1-1mdv2008.0
+ Revision: 24098
- Import ac3info

