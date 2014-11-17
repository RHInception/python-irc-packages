# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-irc
Version:        11.0.1
Release:        1%{?dist}
Summary:        IRC protocol library for Python

License:        MIT
URL:            http://python-irclib.sourceforge.net
Source0:        https://pypi.python.org/packages/source/i/irc/irc-11.0.1.zip

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-more-itertools, python-jaraco-util


%description
IRC protocol library for Python.

%prep
%setup -q -n irc-%{version}


%build

%{__sed} -i 's|use_hg_version=True|version="%{version}"|' setup.py
%{__sed} -i "s|        'hgtools',||" setup.py
%{__sed} -i "s|        'pytest-runner',||" setup.py
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc README.rst LICENSE COPYING
# For noarch packages: sitelib
%{python_sitelib}/*
%exclude %{python_sitelib}/irc/tests

%changelog
* Mon Nov 17 2014 Steve Milner <stevem@gnulinux.net> - 11.0.1-1
- Big version bump.

* Wed Jun  4 2014 Tim Bielawa <tbielawa@redhat.com> - 8.9.1-3
- Don't include unittests in production RPM

* Wed Jun  4 2014 Tim Bielawa <tbielawa@redhat.com> - 8.9.1-2
- Add buildrequires on python-setuptools

* Wed Jun  4 2014 Steve Milner <stevem@gnulinux.net> - 8.9.1-1
- Initial spec.
