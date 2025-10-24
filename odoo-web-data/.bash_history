./odoo-bin -d tu_base --dev=all
cd /usr/src/odoo
exit
find / -name "odoo-bin" 2>/dev/null
python3 -m pip show odoo
exit
odoo -d TEST -u gestion_estudiantes --stop-after-init --log-level=debug
ls /mnt/extra-addons/gestion_estudiantes
exit
odoo -d TEST -u gestion_estudiantes --stop-after-init
odoo -d TEST -u gestion_estudiantes --stop-after-init --log-level=debug
psql -U odoo -d TEST -c "SELECT name, latest_version, state FROM ir_module_module WHERE name='gestion_estudiantes';"
exit
