#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-microbenchmark
Version  : 1.4.2.1
Release  : 32
URL      : http://cran.r-project.org/src/contrib/microbenchmark_1.4-2.1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/microbenchmark_1.4-2.1.tar.gz
Summary  : Accurate Timing Functions
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-microbenchmark-lib
Requires: R-ggplot2
BuildRequires : R-ggplot2
BuildRequires : clr-R-helpers

%description
the execution time of R expressions.

%package lib
Summary: lib components for the R-microbenchmark package.
Group: Libraries

%description lib
lib components for the R-microbenchmark package.


%prep
%setup -q -c -n microbenchmark

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502409451

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502409451
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library microbenchmark
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library microbenchmark
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library microbenchmark
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/microbenchmark/DESCRIPTION
/usr/lib64/R/library/microbenchmark/INDEX
/usr/lib64/R/library/microbenchmark/LICENSE
/usr/lib64/R/library/microbenchmark/Meta/Rd.rds
/usr/lib64/R/library/microbenchmark/Meta/features.rds
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
/usr/lib64/R/library/microbenchmark/libs/symbols.rds
/usr/lib64/R/library/microbenchmark/tests/test_regression.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/microbenchmark/libs/microbenchmark.so
/usr/lib64/R/library/microbenchmark/libs/microbenchmark.so.avx2
