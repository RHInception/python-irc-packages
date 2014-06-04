# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-jaraco-util
Version:        10.0.2
Release:        1%{?dist}
Summary:        General utility module that supplies commonly-used functionality

License:        MIT
URL:            http://pypi.python.org/pypi/jaraco.util
Source0:        https://pypi.python.org/packages/source/j/jaraco.util/jaraco.util-10.0.2.zip

BuildArch:      noarch
BuildRequires:  python-devel

%description
General utility module that supplies commonly-used functionality

%prep
%setup -q -n jaraco.util-%{version}


%build
sed -i "s|#!python||" jaraco/lang/python.py
sed -i "s|#!/usr/bin/env python||" jaraco/util/filesystem.py
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README.txt
# For noarch packages: sitelib
%{python_sitelib}/*
%exclude %{_bindir}/calc-prorate
%exclude %{_bindir}/roll-dice

%changelog
* Wed Jun  4 2014 Steve Milner <stevem@gnulinux.net> - 10.0.2-1
- Initial spec.
