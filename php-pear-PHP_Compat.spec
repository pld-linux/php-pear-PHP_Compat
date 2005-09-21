%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Compat
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides missing functionality for older versions of PHP
Summary(pl):	%{_pearname} - dostarczenie brakuj±cej funkcjonalno¶ci dla starszych wersji PHP
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	1.3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b67c0a9fb20c0df0bac7f4759b48b088
URL:		http://pear.php.net/package/PHP_Compat/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 4:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_Compat provides missing functionality in the form of Constants and
Functions for older versions of PHP.

Constants:
- E_STRICT
- PATH_SEPERATOR
- ...

Functions:
- file_get_contents
- file_put_contents
- is_a
- scandir
- array_combine
- ...

In PEAR status of this package is: %{_status}.

%description -l pl
PHP_Compat dostarcza (w postaci sta³ych oraz funkcji) brakuj±cej
funkcjonalno¶ci dla starszych wersji PHP.

Sta³e:
- E_STRICT
- PATH_SEPERATOR
- ...

Funkcje:
- file_get_contents
- file_put_contents
- is_a
- scandir
- array_combine
- ...

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
