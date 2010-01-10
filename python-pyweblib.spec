Name:           python-pyweblib
Version:        1.3.6
Release:        %mkrel 1
Epoch:          0
Summary:        Yet another web programming framework for Python
License:        GPL
Group:          Development/Python
URL:            http://www.stroeder.com/pylib/PyWebLib/
Source0:        http://www.stroeder.com/pylib/PyWebLib/download/pyweblib-%{version}.tar.gz
%py_requires -d
BuildArch:      noarch
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

