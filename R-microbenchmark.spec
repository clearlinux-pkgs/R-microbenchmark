#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-microbenchmark
Version  : 1.4
Release  : 14
URL      : http://cran.r-project.org/src/contrib/microbenchmark_1.4-2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/microbenchmark_1.4-2.tar.gz
Summary  : Accurate Timing Functions
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-ggplot2
BuildRequires : R-ggplot2
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n microbenchmark

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library microbenchmark
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library microbenchmark


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/microbenchmark/DESCRIPTION
/usr/lib64/R/library/microbenchmark/INDEX
/usr/lib64/R/library/microbenchmark/LICENSE
/usr/lib64/R/library/microbenchmark/Meta/Rd.rds
/usr/lib64/R/library/microbenchmark/Meta/hsearch.rds
/usr/lib64/R/library/microbenchmark/Meta/links.rds
/usr/lib64/R/library/microbenchmark/Meta/nsInfo.rds
/usr/lib64/R/library/microbenchmark/Meta/package.rds
/usr/lib64/R/library/microbenchmark/NAMESPACE
/usr/lib64/R/library/microbenchmark/R/microbenchmark
/usr/lib64/R/library/microbenchmark/R/microbenchmark.rdb
/usr/lib64/R/library/microbenchmark/R/microbenchmark.rdx
/usr/lib64/R/library/microbenchmark/help/AnIndex
/usr/lib64/R/library/microbenchmark/help/aliases.rds
/usr/lib64/R/library/microbenchmark/help/microbenchmark.rdb
/usr/lib64/R/library/microbenchmark/help/microbenchmark.rdx
/usr/lib64/R/library/microbenchmark/help/paths.rds
/usr/lib64/R/library/microbenchmark/html/00Index.html
/usr/lib64/R/library/microbenchmark/html/R.css
/usr/lib64/R/library/microbenchmark/libs/microbenchmark.so
/usr/lib64/R/library/microbenchmark/libs/symbols.rds
/usr/lib64/R/library/microbenchmark/tests/test_regression.R
