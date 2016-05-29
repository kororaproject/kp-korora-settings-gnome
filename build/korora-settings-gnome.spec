%define  debug_package %{nil}

Summary:    Korora configs for GNOME
Name:       korora-settings-gnome
Version:    0.15
Release:    1%{?dist}.1

Group:      System Environment/Base
License:    GPLv3+
Url:        http://kororaproject.org
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch: noarch

Requires:   hack-fonts
Requires(post):   glib2 dconf

Obsoletes:  kororaa-settings-gnome
Provides:   kororaa-settings-gnome

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/dconf/db/local.d

#gnome override
install -m 0644 %{_builddir}/%{name}-%{version}/org.korora.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/org.korora.gschema.override

install -m 0644 00_korora_terminal %{buildroot}%{_sysconfdir}/dconf/db/local.d/00_korora_terminal
#gnome fallback
#install -m 0644 -D %{_builddir}/%{name}-%{version}/gnome-fallback.desktop %{buildroot}%{_datadir}/xsessions/gnome-fallback.desktop

# help icon on desktop
#cd %{buildroot}/
#ln -sf /usr/share/applications/gnome-yelp.desktop %{buildroot}/%{_sysconfdir}/skel/Desktop/Help-gnome.desktop
#cd -

%clean
rm -rf %{buildroot}

%pre

%post
# reload changes
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%postun
# reload changes
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%files
%defattr(-,root,root,-)
%{_datadir}/glib-2.0/schemas/org.korora.gschema.override
%{_sysconfdir}/dconf/db/local.d/00_korora_terminal

%changelog
* Fri May 13 2016 Chris Smart <csmart@kororaproject.org> 0.15-1
- Korora 24

* Wed Feb 10 2016 Chris Smart <csmart@kororaproject.org> 0.14-1
- Add Korora profile to GNOME terminal

* Thu Nov 12 2015 Ian Firns <firnsy@kororaproject.org> 0.13-4
- Added nautilus defaults to reduce icon size by default.

* Wed Nov 4 2015 Chris Smart <csmart@kororaproject.org> 0.13-3
- Switch default backgrounds to Fedora supplemental wallpapers.

* Fri Jul 31 2015 Ian Firns <firnsy@kororaproject.org> 0.13-2
- Added nemo overides to hide default icons from desktop.

* Wed Jul 29 2015 Ian Firns <firnsy@kororaproject.org> 0.13-1
- Added additional Mate overrides for workspaces.

* Wed Jul 15 2015 Ian Firns <firnsy@kororaproject.org> 0.12-5
- Cleaned up spec file.

* Sun Jun 28 2015 Ian Firns <firnsy@kororaproject.org> 0.12-4
- Added extra tweaks to latest dash-to-dock.

* Sun Jun 28 2015 Ian Firns <firnsy@kororaproject.org> 0.12-3
- No Adwaita theme in cinnamon and panel overrides have moved
  to json structures (thanks leigh123linux).

* Fri Jun 26 2015 Ian Firns <firnsy@kororaproject.org> 0.12-2
- Fixed default backgrounds to no longer use default-animated.

* Sun Jun 14 2015 Ian Firns <firnsy@kororaproject.org> 0.12-1
- Removed legacy cinnamon keys (thanks leigh123linux).

* Sun Apr 12 2015 Ian Firns <firnsy@kororaproject.org> 0.11-5
- Added mouse theme override for MATE and revert compiz on MATE.

* Sun Feb 22 2015 Ian Firns <firnsy@kororaproject.org> 0.11-3
- Fixed compiz session requirements.

* Sun Feb 22 2015 Ian Firns <firnsy@kororaproject.org> 0.11-1
- Updated MATE default in overrides.

* Fri Jan 9 2015 Chris Smart <csmart@kororaproject.org> 0.10-6
- Touchpad: enable touch to click by default

* Fri Jan 9 2015 Chris Smart <csmart@kororaproject.org> 0.10-5
- Cinnamon fix: align open applications in taskbar to left in Cinnamon
- Thanks leigh123linux

* Wed Dec 31 2014 Ian Firns <firnsy@kororaproject.org> 0.10-3
- Enable dash-to-dock in Gnome

* Sun Dec 28 2014 Chris Smart <csmart@kororaproject.org> 0.10-2
- Cinnamon settings for Korora 21 release

* Sat Dec 20 2014 Chris Smart <csmart@kororaproject.org> 0.10-1
- Move firefox profile to korora-extras package.

* Sat Dec 20 2014 Chris Smart <csmart@kororaproject.org> 0.8-1
- Building for K21

* Tue Oct 14 2014 Ian Firns <firnsy@kororaproject.org> 0.7.1-1
- Fixed issue adding applets to Cinnamon menu

* Sat May 3 2014 Chris Smart <csmart@kororaproject.org> 0.7-10
- Update mozilla default profile to support adblock-plus 2.6

* Wed Mar 12 2014 Chris Smart <csmart@kororaproject.org> 0.7-9
- Update mozilla default profile to support adblock-plus 2.5.1

* Fri Dec 27 2013 Chris Smart <csmart@kororaproject.org> 0.7-8
- Updated some more setting changes for Cinnamon
- set desktop to flipped, fixed hotspots, fixed theme

* Fri Sep 26 2013 Chris Smart <csmart@kororaproject.org> 0.7-7
- Updated settings for Cinnamon 2.0

* Fri Sep 06 2013 Chris Smart <csmart@kororaproject.org> 0.7-6
- Add settings for Cinnamon and MATE desktop to overrides file

* Sun Aug 18 2013 Chris Smart <csmart@kororaproject.org> 0.7-5
- Add "Software" to the side bar so it's easier for new users to add software

* Mon Jul 29 2013 Chris Smart <csmart@kororaproject.org> 0.7-4
- Disable mouse highlight and desktop icons as these cause problems in GNOME 3.8

* Mon Jun 10 2013 Chris Smart <csmart@kororaproject.org> 0.7-3
- Remove the mimeapps.lst file as we now ship shared-mime-info instead,
remove menu file as we don't need to re-arrange things now either.

* Sun Jun 09 2013 Chris Smart <csmart@kororaproject.org> 0.7-2
- Remove the extra desktop files we ship as they aren't needed now thanks 
to GNOME 3 layout, remove old gconf settings, added extra default settings 
such as delete in Files.

* Fri Feb 15 2013 Ian Firns <firnsy@kororaproject.org> 0.7-1
- Added background picture-uri preference."

* Thu Oct 25 2012 Chris Smart <csmart@kororaproject.org> 0.6-1
- Korora 18 build.

* Sat Jun 30 2012 Chris Smart <chris@kororaa.org> 0.5-2
- Added settings for Cinnamon.

* Sun May 20 2012 Chris Smart <chris@kororaa.org> 0.5-1
- Updated build for Kororaa 17 release, remove background slideshow, remove mimelist (override shared-mime-info instead), added GNOME Fallback as session option at log in.

* Tue Nov 29 2011 Chris Smart <chris@kororaa.org> 0.4-3
- Added alternative-status-menu back, now that it does not crash GNOME Shell.

* Tue Nov 29 2011 Chris Smart <chris@kororaa.org> 0.4-2
- Remove Empathy from GNOME favourites, remove K3b shortcuts (replaced by Brasero).

* Sat Oct 29 2011 Chris Smart <chris@kororaa.org> 0.4-1
- Remove old Firefox profiles, cleaned up GNOME menus, added new tweaks to overrides file such as setting favourites in Shell.

* Sun Oct 23 2011 Chris Smart <chris@kororaa.org> 0.3-8
- Fix issue where user Firefox settings aren't applied.

* Wed Oct 12 2011 Chris Smart <chris@kororaa.org> 0.3-7
- Point Firefox profile to new location.

* Tue Oct 11 2011 Chris Smart <chris@kororaa.org> 0.3-6
- Removed shortcut to gnome-theme-properties, which no-longer exists in GNOME 3.

* Wed Oct 11 2011 Chris Smart <chris@kororaa.org> 0.3-5
- Renamed GNOME Desktop Switcher command to make its function more clear.

* Mon Oct 3 2011 Chris Smart <chris@kororaa.org> 0.3-4
- Turn off default touchpad settings (disable while typing, etc) as some users reporting mouse freeze. Added support for Firefox 8.

* Sun Sep 18 2011 Chris Smart <chris@kororaa.org> 0.3-3
- Set GNOME 3 Shell to have only maximise and close buttons, Fallback mode to also have minimise.

* Sat Sep 17 2011 Chris Smart <chris@kororaa.org> 0.3-2
- Added desktop switcher for GNOME 3.

* Sun Aug 21 2011 Chris Smart <chris@kororaa.org> 0.3-1
- Updated for Firefox 6 and 7.

* Wed Aug 3 2011 Chris Smart <chris@kororaa.org> 0.2-4
- Overwrite default start page to Firefox default.

* Tue Jul 26 2011 Chris Smart <chris@kororaa.org> 0.2-3
- Removed Firefox4 desktop entry, not required for F15, added GNOME switching desktop script

* Thu Jul 14 2011 Chris Smart <chris@kororaa.org> 0.2-2
- Changes for 15 release (GNOME 3)

* Wed Apr 27 2011 Chris Smart <chris@kororaa.org> 0.1-5
- Modified to create arch specific packages, to fix firefox prefs issue.

* Tue Apr 26 2011 Chris Smart <chris@kororaa.org> 0.1-4
- Set abstract slideshow background for GNOME

* Mon Apr 25 2011 Chris Smart <chris@kororaa.org> 0.1-3
- Custom application menu for GNOME

* Tue Mar 05 2011 Chris Smart <chris@kororaa.org> 0.1-1
- Initial spec, taken from kororaa-extras, removed downloadstatusbar

