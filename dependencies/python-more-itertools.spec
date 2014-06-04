# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-more-itertools
Version:        2.2
Release:        1%{?dist}
Summary:        More routines for operating on iterables, beyond itertools

License:        MIT
uRL:            https://github.com/erikrose/more-itertools/
Source0:        https://pypi.python.org/packages/source/m/more-itertools/more-itertools-2.2.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel

%description
A collection of several routines for working with iterables.

%prep
%setup -q -n more-itertools-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc LICENSE README.rst
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Wed Jun  4 2014 Steve Milner <stevem@gnulinux.net> - 2.2-1
- Created initial spec 
