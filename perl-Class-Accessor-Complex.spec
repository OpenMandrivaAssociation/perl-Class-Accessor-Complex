%define upstream_name    Class-Accessor-Complex
%define upstream_version 1.100880

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Arrays, hashes, booleans, integers, sets and more
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Accessor::Installer)
BuildRequires:	perl(Data::Miscellany)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.100.880-2mdv2011.0
+ Revision: 654890
- rebuild for updated spec-helper

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.880-1mdv2011.0
+ Revision: 530233
- update to 1.100880

* Sun Mar 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.820-2mdv2010.1
+ Revision: 528513
- ship meta.yml

* Wed Mar 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.820-1mdv2010.1
+ Revision: 527093
- update to 1.100820

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.1
+ Revision: 474660
- update to 0.16

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 444079
- import perl-Class-Accessor-Complex


* Thu Sep 17 2009 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist
