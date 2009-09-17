%define upstream_name    Class-Accessor-Complex
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Arrays, hashes, booleans, integers, sets and more
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::Accessor::Installer)
BuildRequires: perl(Data::Miscellany)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module generates accessors for your class in the same spirit as the
Class::Accessor manpage does. While the latter deals with accessors for
scalar values, this module provides accessor makers for arrays, hashes,
integers, booleans, sets and more.

As seen in the synopsis, you can chain calls to the accessor makers. Also,
because this module inherits from the Class::Accessor manpage, you can put
a call to one of its accessor makers at the end of the chain.

The accessor generators also generate documentation ready to be used with
the Pod::Generated manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


