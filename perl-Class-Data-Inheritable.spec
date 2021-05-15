%bcond_without perl_Class_Data_Inheritable_enables_optional_test
Name:                perl-Class-Data-Inheritable
Version:             0.08
Release:             1
Summary:             Inheritable, overridable class data
License:             GPL+ or Artistic
URL:                 https://metacpan.org/release/Class-Data-Inheritable
Source0:             Class-Data-Inheritable-%{version}-clean.tar.gz
BuildArch:           noarch
BuildRequires:       coreutils findutils make perl-generators perl-interpreter
BuildRequires:       perl(ExtUtils::MakeMaker) perl(Carp) perl(strict) perl(vars) perl(base)
BuildRequires:       perl(Test::More)
%if %{with perl_Class_Data_Inheritable_enables_optional_test}
BuildRequires:       perl(Test::Pod) >= 1.00 perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:            perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version)) perl(Carp)
%description
Class::Data::Inheritable is for creating accessor/mutators to
class data. That is, if you want to store something about your
class as a whole (instead of about a single object). This data
is then inherited by your sub-classes and can be overridden.

%prep
%setup -q -n Class-Data-Inheritable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Data::Inheritable.3pm*

%changelog
* Fri May 14 2021 xxxxxx <xxxxxx@huawei.com> - 0.08-1
- package init
