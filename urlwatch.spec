Summary:	Tool for monitoring webpages for updates
Summary(pl.UTF-8):	Narzędzie do obserwacji stron www w poszukiwaniu aktualizacji
Name:		urlwatch
Version:	1.8
Release:	1
License:	distributable
Group:		Applications
Source0:	http://thpinfo.com/2008/urlwatch/%{name}-%{version}.tar.gz
# Source0-md5:	358f3b82a2c762c713b513bc0e5622b6
Patch0:		%{name}-useless_files.patch
URL:		http://thpinfo.com/2008/urlwatch/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
urlwatch is a script intended to help you watch URLs and get notified
(via email) of any changes. The change notification will include the
URL that has changed and a unified diff of what has changed. It is
typically run as a cronjob.

%description -l pl.UTF-8
urlwatch to skrypt, który ma na celu informowanie użytkownika
(poprzez email) o wszelkich zmianach dokonanych na stronach www.
Powiadomienie zawiera wyłącznie informacje o stronach, które
uległy zmianie w postaci listy różnic (diff). Zazwyczaj uruchamiany
jest jako zadanie crona.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING must be added
%doc COPYING ChangeLog PKG-INFO examples/*.example
%attr(755,root,root) %{_bindir}/urlwatch
%{_mandir}/man1/urlwatch.1*
%dir %{py_sitescriptdir}/urlwatch
%{py_sitescriptdir}/urlwatch/*.py[co]
%{py_sitescriptdir}/*.egg-info
