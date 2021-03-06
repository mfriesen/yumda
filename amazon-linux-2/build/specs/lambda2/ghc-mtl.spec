# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name mtl

Name:           ghc-%{pkg_name}
# part of haskell-platform
Version:        2.1.2
Release:        27%{?dist}
Summary:        Monad classes using functional dependencies

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

Prefix: %{_prefix}

%description
Monad classes using functional dependencies, with instances for various monad
transformers, inspired by the paper "Functional Programming with Overloading
and Higher-Order Polymorphism", by Mark P Jones, in "Advanced School of
Functional Programming", 1995
(<http://web.cecs.pdx.edu/~mpj/pubs/springschool.html>).


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install

for file in $(grep -v package.conf.d %{name}-devel.files); do rm -rf %{buildroot}$file || :; done


%files -f %{name}.files
%license LICENSE
%exclude %{ghclibdir}/package.conf.d


%changelog
* Wed May 15 2019 Michael Hart <michael@lambci.org>
- recompiled for AWS Lambda (Amazon Linux 2) with prefix /opt

* Wed Dec  4 2013 Jens Petersen <petersen@redhat.com> - 2.1.2-27
- bump release

* Wed Oct 16 2013 Jens Petersen <petersen@redhat.com> - 2.1.2-26
- add static provides to devel

* Sun Sep  8 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.1.2-25
- spec file generated by cabal-rpm-0.8.3
- revive src package instead of subpackaging in haskell-platform

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 2.0.1.0-11
- rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Jens Petersen <petersen@redhat.com> - 2.0.1.0-9
- update to cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.0.1.0-8.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.0.1.0-8.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 2.0.1.0-8.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 2.0.1.0-8
- ghc_arches replaces ghc_excluded_archs

* Sun Jun 19 2011 Jens Petersen <petersen@redhat.com> - 2.0.1.0-7
- BR ghc-Cabal-devel instead of ghc-prof
- use ghc_excluded_archs

* Fri May 27 2011 Jens Petersen <petersen@redhat.com> - 2.0.1.0-6
- update to cabal2spec-0.23

* Thu May 05 2011 Jiri Skala <jskala@redhat.com> - 2.0.1.0-5
- Enable build on ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.0.1.0-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Jens Petersen <petersen@redhat.com> - 2.0.1.0-2
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 2.0.1.0-1
- update to mtl 2.0.1.0 for ghc7
- depends on transformers

* Wed Nov 24 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.2-9
- drop the -o obsoletes

* Sat Sep  4 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.2-8
- update to latest macros, hscolour and drop doc pkg (cabal2spec-0.22.2)
- part of haskell-platform-2010.2.0.0

* Wed Jun 23 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.2-7
- use ghc_strip_dynlinked (ghc-rpm-macros-0.6.0)

* Sat Apr 24 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.2-6
- part of haskell-platform-2010.1.0.0
- rebuild against ghc-6.12.2
- condition ghc_lib_package

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.2-5
- bump release above the temporary ghc mtl subpackages

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.2-2
- update to ghc-rpm-macros-0.5.1: use ghc_lib_package
- drop bcond for doc and prof
- add comment about haskell-platform

* Thu Dec 24 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.2-1
- update packaging for ghc-6.12.1
- added shared library support
- use new ghc*_requires macros: needs ghc-rpm-macros 0.4.0

* Wed Dec 23 2009 Fedora Haskell SIG <fedora-haskell-list@redhat.com> - 1.1.0.2-0
- initial packaging for Fedora automatically generated by cabal2spec-0.19
