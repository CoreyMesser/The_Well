#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from character_pc import PlayerCharacter, Species, HealthPoints, Stats, CharacterSkillsGenerator, MeritsFlawsGenerator, POCC, SOCC, CharacterStoreSession
from templates.template_text import Templates, CharacterControlTemplates
from services import PrinterServices, PrintCompletedCharacterSheet
from services_navigation import CharacterNavigation
from services_get_character import GetCharacter
from models import CharacterModels, User
from database_service import db_session
from config import Config

from flask import Flask
from flask import Flask, render_template, g, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_wtf import Form

from forms import CharacterForm, RegisterForm, LoginForm
import models

from app import get_app

import curses

app = get_app()
db = db_session()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/character_creation', methods=('GET', 'POST'))
def character_creation_form():
    form = CharacterForm()
    if form.validate_on_submit():
        pass
    return render_template('character_creation.html', form=form)


@login_manager.user_loader
def load_user(userid):
    try:
        return db.query(User).filter_by(id=userid).first()
    except models.DoesNotExist:
        return None


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        flash("Yay, you registered!", "success")
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = db.query(User).filter_by(user_email=form.email.data).first()
        except Exception as e:
            flash("Soemthing went wrong {}".format(e))
        else:
            if user.password_hash == form.password.data:
                login_user(user)
                flash("You've been logged in!", "success")
                return redirect(url_for('index'))
            elif check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("You've been logged in!", "success")
                return redirect(url_for('index'))
            else:
                flash("Your credentials are wrong.")
        # flash('you have logged in', (form.email.data, form.password.data, form.remeber_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out! Come back soon!", "success")
    return redirect(url_for('index'))


class Introduction(object):
    def intro(self):
        print(Templates.BANNER)
        print(Templates.INTRO)
        input('ᗛᗛᗛ Press Return to continue ᗘᗘᗘ')
        # cc = CharacterCreation()
        # cc.__init__()
        gg = Gameplay()
        ci = CursesInitializer()
        ci.__init__()
        gg.__init__()


class CursesInitializer(object):

    def __init__(self):
        self.myscreen = curses.initscr()
        self.win = curses.newwin(25, 50, 20, 20)

        self.myscreen.border(0)
        self.myscreen.addstr(25, 50)
        self.myscreen.refresh()
        self.myscreen.getch()

        # curses.endwin()

class CharacterCreation(object):

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        self.template = Templates()
        self.hp = HealthPoints()
        self.pc = PlayerCharacter()
        self.sp = Species()
        self.sts = Stats()
        self.sk = CharacterSkillsGenerator()
        self.mf = MeritsFlawsGenerator()
        self.po = POCC()
        self.so = SOCC()
        self.ps = PrinterServices()
        self.db_cs = CharacterStoreSession()
        self.chs_ex = CharacterSheetExportOptions()
        self.character_dict = self.pc.character_dict
        self.skills_dict = self.pc.skills_dict
        self.character_creation()

    def character_creation(self):
        finished = False

        while finished is False:
            return_menu = False
            self.clear_screen()
            self.hp.update_hp()
            print(self.ps.print_char_sheet(self.character_dict, self.skills_dict))
            print('\n'+'\/'*20+'\n \n')
            player_choice = input("ᗘᗘᗘ Please Enter the stat you would like to adjust: \n >> ").lower()
            if player_choice == 'name':
                self.character_dict['name'] = input(self.template.NAME)
            if player_choice == 'sex':
                self.character_dict['sex'] = input(self.template.SEX)
            if player_choice == 'species':
                species = input(self.template.SPECIES).upper()
                self.ps.print_species_list(species)
                species_l_choice = input(self.template.SPECIES_SELECT).upper()
                return_menu = self.sp.get_species(species=species, species_l_choice=species_l_choice)
            if player_choice == 'faction':
                self.character_dict['faction'] = input(self.template.FACTIONS)
            if player_choice == 'alg':
                self.character_dict['alg'] = input(self.template.ALIGNMENT)
            if player_choice == 'pocc':
                self.po.print_pocc()
                select_pocc = input(self.template.SELECT_POCC).lower()
                self.po.get_pocc(select_pocc=select_pocc)
            if player_choice == 'socc':
                self.so.check_required_pocc()
            if player_choice == 'hp':
                hp_adjust = self.hp.get_hp_player_choice()
                self.hp.get_hp(hp_adjust=hp_adjust)
            if player_choice in self.pc.character_stats:
                self.sts.get_stats(player_choice)
            if player_choice == 'skills':
                while return_menu is False:
                    return_menu = self.sk.get_skills()
            if player_choice == 'merits':
                while return_menu is False:
                    return_menu = self.mf.get_merits()
            if player_choice == 'flaws':
                while return_menu is False:
                    return_menu = self.mf.get_flaws()
            if player_choice == 'finished':
                finished = True

        char_id, char_name = self.db_cs.store_character_session()
        self.chs_ex.export_character_sheet_txt(char_id=char_id, char_name=char_name)
        self.chs_ex.create_another_character()


class Gameplay(object):

    def __init__(self):
        self.cn = CharacterNavigation()
        self.cctemp = CharacterControlTemplates()
        self.gc = GetCharacter()
        self.player_move_dict = self.retreive_character()
        self.setup()
        self.player_controls()

    def setup(self):
        self.cn.start_location(player_move_dict=self.player_move_dict)

    def retreive_character(self):
        # retrieves character from database and creates a stripped down model to use in-game
        player_move_dict = CharacterModels.PLAYER_MOVE_DICT
        return player_move_dict

    def player_controls(self):
        finished = False

        while finished is False:
            return_menu = False
            player_choice = input(self.cctemp.PLAYER_CHOICE).upper()
            if player_choice == 'HELP':
                print(self.cctemp.PLAYER_HELP)
            if player_choice == 'LOOK':
                pass
            if player_choice == 'SEARCH':
                pass
            if player_choice == 'USE':
                pass
            if player_choice == 'TAKE':
                pass
            if player_choice == 'TURN':
                player_choice = input(self.cctemp.PLAYER_DIRECTIONS).upper()
                self.cn.get_player_direction(player_choice=player_choice)
            if player_choice == 'MOVE':
                player_choice = input(self.cctemp.PLAYER_MOVE).upper()
                self.cn.move_player(player_choice=player_choice)
            if player_choice == 'CLIMB':
                pass
            if player_choice == 'JUMP':
                pass
            if player_choice == 'INVENTORY':
                pass
            if player_choice == 'EQUIP':
                pass
            if player_choice == 'UNEQUIP':
                pass
            if player_choice == 'ATTACK':
                pass
            if player_choice == 'BLOCK':
                pass
            if player_choice == 'FLEE':
                pass


class CharacterSheetExportOptions(object):
    ps = PrintCompletedCharacterSheet()
    template = Templates()

    def export_character_sheet_txt(self, char_id, char_name):
        exit_sheet = False

        while exit_sheet is False:
            player_choice = input("Would you like to save your Character to file? [YES] [NO] >>").upper()
            if player_choice == 'YES':
                self.ps.print_character_sheet_from_db(char_id=char_id)
                exit_sheet = True
            elif player_choice == 'NO':
                player_confirm = input("You character {}'s ID is {}.  Please keep that handy. Are you sure you would like to QUIT "
                                       "without saving? [YES] [NO]>>".format(char_id, char_name)).upper()
                if player_confirm == 'NO':
                    self.ps.print_character_sheet_from_db(char_id=char_id)
                elif player_confirm == 'YES':
                    exit_sheet = True
                else:
                    print(self.template.VALID_ENTRY)
            else:
                print(self.template.VALID_ENTRY)

    def create_another_character(self):
        cc = CharacterCreation()
        template = Templates()
        exit_sheet = False

        while exit_sheet is False:
            player_choice = input("Would you like to create another character? [YES] [NO] >>").upper()
            if player_choice == 'YES':
                cc.character_creation()
            elif player_choice == 'NO':
                print(template.GOODBYE)
                exit_sheet = True
            else:
                print(self.template.VALID_ENTRY)
