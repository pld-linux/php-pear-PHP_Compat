%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Compat
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides missing functionality for older versions of PHP
Summary(pl):	%{_pearname} - dostarczenie brakującej funkcjonalności dla starszych wersji PHP
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	34e3815c995189e00e2a6eaf093c6fe6
URL:		http://pear.php.net/package/PHP_Compat/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_Compat provides missing functionality in the form of Constants and
Functions for older versions of PHP.

Constants:
- E_STRICT
- PATH_SEPERATOR

Functions:
- file_get_contents
- file_put_contents
- is_a
- scandir
- array_combine

In PEAR status of this package is: %{_status}.

%description -l pl
PHP_Compat dostarcza (w postaci stałych oraz funkcji) brakującej
funkcjonalności dla starszych wersji PHP.

Stałe:
- E_STRICT
- PATH_SEPERATOR

Funkcje:
- file_get_contents
- file_put_contents
- is_a
- scandir
- array_combine

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Function,Constant}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/Constant/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Constant
install %{_pearname}-%{version}/%{_subclass}/Function/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Function

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/
