Name:           perl-Exporter
Version:        5.68
Release:        3%{?dist}
Summary:        Implements default import method for modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Exporter/
Source0:        http://www.cpan.org/authors/id/T/TO/TODDR/Exporter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp) >= 1.05
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
%if !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.18
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp) >= 1.05
Requires:       perl(warnings)

Prefix: %{_prefix}

%description
The Exporter module implements an import method which allows a module to
export functions and variables to its users' name spaces. Many modules use
Exporter rather than implementing their own import method because Exporter
provides a highly flexible interface, with an implementation optimized for
the common case.

%prep
%setup -q -n Exporter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor \
  PREFIX=%{_prefix} \
  INSTALLVENDORLIB=%{perl_vendorlib} \
  INSTALLVENDORARCH=%{perl_vendorarch}
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%license README
%{perl_vendorlib}/*

%exclude %{_mandir}

%changelog
* Wed May 15 2019 Michael Hart <michael@lambci.org>
- recompiled for AWS Lambda (Amazon Linux 2) with prefix /opt

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 5.68-3
- Mass rebuild 2013-12-27

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 5.68-2
- Specify all dependencies

* Thu Mar 28 2013 Petr Pisar <ppisar@redhat.com> - 5.68-1
- 5.68 bump

* Fri Mar 22 2013 Petr Pisar <ppisar@redhat.com> 5.67-1
- Specfile autogenerated by cpanspec 1.78.
