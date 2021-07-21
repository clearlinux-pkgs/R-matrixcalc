#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-matrixcalc
Version  : 1.0.4
Release  : 35
URL      : https://cran.r-project.org/src/contrib/matrixcalc_1.0-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/matrixcalc_1.0-4.tar.gz
Summary  : Collection of Functions for Matrix Calculations
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
for probability, econometric and numerical analysis. There are
        additional functions that are comparable to APL functions which
        are useful for actuarial models such as pension mathematics.
        This package is used for teaching and research purposes at the
        Department of Finance and Risk Engineering, New York
        University, Polytechnic Institute, Brooklyn, NY 11201.
        Horn, R.A. (1990) Matrix Analysis. ISBN 978-0521386326.
        Lancaster, P. (1969) Theory of Matrices. ISBN 978-0124355507.

%prep
%setup -q -c -n matrixcalc
cd %{_builddir}/matrixcalc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622737639

%install
export SOURCE_DATE_EPOCH=1622737639
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library matrixcalc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library matrixcalc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library matrixcalc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc matrixcalc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/matrixcalc/DESCRIPTION
/usr/lib64/R/library/matrixcalc/INDEX
/usr/lib64/R/library/matrixcalc/Meta/Rd.rds
/usr/lib64/R/library/matrixcalc/Meta/features.rds
/usr/lib64/R/library/matrixcalc/Meta/hsearch.rds
/usr/lib64/R/library/matrixcalc/Meta/links.rds
/usr/lib64/R/library/matrixcalc/Meta/nsInfo.rds
/usr/lib64/R/library/matrixcalc/Meta/package.rds
/usr/lib64/R/library/matrixcalc/NAMESPACE
/usr/lib64/R/library/matrixcalc/R/matrixcalc
/usr/lib64/R/library/matrixcalc/R/matrixcalc.rdb
/usr/lib64/R/library/matrixcalc/R/matrixcalc.rdx
/usr/lib64/R/library/matrixcalc/help/AnIndex
/usr/lib64/R/library/matrixcalc/help/aliases.rds
/usr/lib64/R/library/matrixcalc/help/matrixcalc.rdb
/usr/lib64/R/library/matrixcalc/help/matrixcalc.rdx
/usr/lib64/R/library/matrixcalc/help/paths.rds
/usr/lib64/R/library/matrixcalc/html/00Index.html
/usr/lib64/R/library/matrixcalc/html/R.css
