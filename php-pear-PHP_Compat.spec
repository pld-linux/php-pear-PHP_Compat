%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Compat
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides missing functionality for older versions of PHP
Summary(pl.UTF-8):   %{_pearname} - dostarczenie brakującej funkcjonalności dla starszych wersji PHP
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4d73c451f4f3a8f9a0516bd26af7f652
URL:		http://pear.php.net/package/PHP_Compat/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
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

%description -l pl.UTF-8
PHP_Compat dostarcza (w postaci stałych oraz funkcji) brakującej
funkcjonalności dla starszych wersji PHP.

Stałe:
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
