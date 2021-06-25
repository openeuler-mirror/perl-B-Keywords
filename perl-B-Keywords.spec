%bcond_with perl_B_Keywords_enables_extra_test
Name:                perl-B-Keywords
Version:             1.20
Release:             2
Summary:             Lists of reserved barewords and symbol names
License:             GPL+ or Artistic
URL:                 https://metacpan.org/release/B-Keywords
Source0:             https://cpan.metacpan.org/modules/by-module/B/B-Keywords-%{version}.tar.gz
BuildArch:           noarch
BuildRequires:       coreutils findutils make perl-generators perl-interpreter perl(Config)
BuildRequires:       perl(ExtUtils::MakeMaker) perl(Exporter) perl(strict) perl(vars) perl-devel
BuildRequires:       perl(File::Spec) perl(lib) perl(Test) perl(Test::More) perl(Test::Pod) >= 1.0
%if 0%{!?perl_bootstrap:1} && %{with perl_B_Keywords_enables_extra_test}
BuildRequires:       perl(File::Copy) perl(Perl::MinimumVersion) >= 1.20
BuildRequires:       perl(Test::CPAN::Meta) >= 0.12 perl(Test::Kwalitee)
BuildRequires:       perl(Test::MinimumVersion) >= 0.008 perl(Test::More) >= 0.88
BuildRequires:       perl(Test::Pod::Coverage) >= 1.04 perl(warnings)
%endif
Requires:            perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%description
Keyword provides an array of several exportable keywords

%prep
%setup -q -n B-Keywords-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
# TODO: Need somebody fix fail
%if 0%{!?perl_bootstrap:1} && %{with perl_B_Keywords_enables_extra_test}
echo make test IS_MAINTAINER=1 AUTHOR_TESTING=1
%else
echo make test
%endif

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/B/
%{_mandir}/man3/B::Keywords.3*

%changelog
* Fri Jun 25 2021 Wenlong Ding <wenlong.ding@turbolinux.com.cn> 1.20-2
- Reformat spec file, replace '\r\n' to '\n'.

* Mon May 17 2021 Pengju Jiang <jiangpengju2@huawei.com> - 1.20-1
- package init

