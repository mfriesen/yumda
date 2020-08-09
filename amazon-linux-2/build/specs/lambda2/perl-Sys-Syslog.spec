Name:           perl-Sys-Syslog
Version:        0.33
Release: 3%{?dist}.0.2
Summary:        Perl interface to the UNIX syslog(3) calls
# Unused sources fallback/* are covered with BSD license.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sys-Syslog/
Source0:        http://www.cpan.org/authors/id/S/SA/SAPER/Sys-Syslog-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(strict)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# DynaLoader not used
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap}
%if !0%{?rhel}
BuildRequires:  perl(Test::Distribution)
%endif
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.06
BuildRequires:  perl(Test::Portability::Files)
# POE::Component::Server::Syslog is not packaged yet
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Fcntl)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Sys::Syslog is an interface to the UNIX syslog(3) function. Call syslog() with
a string priority and a list of printf() arguments just like at syslog(3).

%prep
%setup -q -n Sys-Syslog-%{version}
chmod -x eg/*
# Inhibit bundled syslog.h
rm -rf fallback
sed -i -e '/^fallback\//d' MANIFEST
# Recode files
for F in Changes; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" >"${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes eg README 
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.33-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.33-2
- Mass rebuild 2013-12-27

* Fri May 24 2013 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Tue Apr 09 2013 Petr Pisar <ppisar@redhat.com> 0.32-1
- Specfile autogenerated by cpanspec 1.78.
