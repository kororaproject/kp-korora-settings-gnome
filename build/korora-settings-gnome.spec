%define  debug_package %{nil}

Summary:    Korora configs for GNOME
Name:       korora-settings-gnome
Version:    0.10
Release:    4%{?dist}.1

Group:      System Environment/Base
License:    GPLv3+
Url:        http://kororaproject.org
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch: noarch

Requires(post):   glib2

Obsoletes:  kororaa-settings-gnome
Provides:   kororaa-settings-gnome

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
#mkdir -p %{buildroot}%{_datadir}/applications/
#mkdir -p %{buildroot}/usr/local/share/applications/
#mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
#mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/profile
#mkdir -p %{buildroot}%{_datadir}/backgrounds/abstract
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
mkdir -p %{buildroot}%{_bindir}
#mkdir -p %{buildroot}%{_sysconfdir}/skel/Desktop

#repackage shared-mime-info instead?
#cp -a %{_builddir}/%{name}-%{version}/mimeapps-gnome.list %{buildroot}%{_datadir}/applications/
#install -m 0644 %{_builddir}/%{name}-%{version}/applications/* %{buildroot}/usr/local/share/applications/
#install -m 0644 %{_builddir}/%{name}-%{version}/applications-korora.menu %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged/applications-korora-gnome.menu
#cp -a %{_builddir}/%{name}-%{version}/prefs-gnome.js %{buildroot}%{_libdir}/firefox/browser/defaults/profile/prefs-gnome.js
#install -m 0644 %{_builddir}/%{name}-%{version}/background-slideshow.xml %{buildroot}/%{_datadir}/backgrounds/abstract/background-1.xml
#install -m 0755 %{_builddir}/%{name}-%{version}/switch-gnome-desktop.sh %{buildroot}/%{_bindir}/switch-gnome-desktop.sh
#install -m 0755 %{_builddir}/%{name}-%{version}/switch-gnome-desktop.desktop %{buildroot}/%{_datadir}/applications/switch-gnome-desktop.desktop
#ln -sf /usr/share/applications/switch-gnome-desktop.desktop %{buildroot}/etc/skel/Desktop/switch-gnome-desktop.desktop

#gnome override
install -m 0644 %{_builddir}/%{name}-%{version}/org.korora.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/org.korora.gschema.override

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
#GNOME tweaks
#sudo -u gdm gconftool-2 --set --type string /apps/gdm/simple-greeter/logo_icon_name fedora-logo-sprite 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /apps/gdm/simple-greeter/logo_icon_name fedora-logo-sprite 2>/dev/null
##gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /apps/metacity/general/theme elementary 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /apps/metacity/general/button_layout :minimize,maximize,close 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/interface/gtk_theme elementary 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/interface/icon_theme elementary 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/applications/browser/exec firefox 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/url-handlers/http/command "firefox %s"
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/url-handlers/https/command "firefox %s"
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/url-handlers/about/command "firefox %s"
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/applications/media/exec vlc 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /apps/gnome-power-manager/ui/icon_policy always 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type int /desktop/gnome/peripherals/touchpad/scroll_method 2 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type bool /desktop/gnome/peripherals/touchpad/disable_while_typing true 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type bool /desktop/gnome/peripherals/touchpad/tap_to_click true 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/background/picture_filename /usr/share/backgrounds/abstract/background-1.xml 2>/dev/null
#
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string  /desktop/gnome/shell/windows/button_layout :maximize,close 2>/dev/null
##gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/shell/windows/theme Elementary 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type boolean /desktop/gnome/shell/windows/edge_tiling true 2>/dev/null
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type boolean /apps/gnome-search-tool/show_additional_options true 2>/dev/null
#
#set up default apps and firefox preferences
#cd %{_datadir}/applications/
#ln -sf mimeapps-gnome.list mimeapps.list
#cd %{_libdir}/firefox/browser/defaults/profile/
#ln -sf prefs-gnome.js prefs.js

#load gnome changes
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null

#set yelp to executable to remove gnome warning on shortcut
#chmod a+x /usr/share/applications/gnome-yelp.desktop

%postun
#load gnome changes
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null

# clean up the link on uninstall of this package (not updates though)
#if [ "$1" == "0" ]
#then
#  cd %{_libdir}/firefox/browser/defaults/profile/
#  unlink prefs.js 2>/dev/null
#  cd -
#fi

%files 
%defattr(-,root,root,-)
#%{_datadir}/applications/mimeapps-gnome.list
#%{_libdir}/firefox/browser/defaults/profile/prefs-gnome.js
#%{_sysconfdir}/xdg/menus/applications-merged/applications-korora-gnome.menu
#/usr/local/share/applications
#%{_datadir}/backgrounds/abstract/background-1.xml
%{_datadir}/glib-2.0/schemas/org.korora.gschema.override
#%{_bindir}/switch-gnome-desktop.sh
#%{_datadir}/applications/switch-gnome-desktop.desktop
#%{_sysconfdir}/skel/Desktop/switch-gnome-desktop.desktop
#%{_sysconfdir}/skel/Desktop/Help-gnome.desktop
#%{_datadir}/xsessions/gnome-fallback.desktop

%changelog
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

