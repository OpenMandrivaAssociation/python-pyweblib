Name:           python-pyweblib
Version:        1.3.6
Release:        %mkrel 2
Epoch:          0
Summary:        Yet another web programming framework for Python
License:        GPL
Group:          Development/Python
URL:            http://www.stroeder.com/pylib/PyWebLib/
Source0:        http://www.stroeder.com/pylib/PyWebLib/download/pyweblib-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Web application library:

pyweblib.forms          class library for handling <FORM> input
pyweblib.session        server-side web session handling
pyweblib.helper         misc. stuff useful in CGI-BINs
pyweblib.sslenv         retrieves SSL-related env vars
pyweblib.httphelper     very basic HTTP functions

%prep
%setup -q -n pyweblib-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc CHANGES htdocs/ cgi-bin/
%{python_sitelib}/*



%changelog
* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0:1.3.6-2mdv2011.0
+ Revision: 593156
- py-devel not required
- rebuild for py2.7

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0:1.3.6-1mdv2010.1
+ Revision: 489191
- update to new version 1.3.6

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0:1.3.5-1mdv2010.0
+ Revision: 384255
- update to new version 1.3.5

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0:1.3.4-6mdv2009.1
+ Revision: 324095
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:1.3.4-5mdv2009.0
+ Revision: 259774
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0:1.3.4-4mdv2009.0
+ Revision: 247625
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 29 2007 David Walluck <walluck@mandriva.org> 0:1.3.4-2mdv2008.1
+ Revision: 103621
- use %%{__python} macro

* Mon Oct 29 2007 David Walluck <walluck@mandriva.org> 0:1.3.4-1mdv2008.1
+ Revision: 103614
- import python-pyweblib


