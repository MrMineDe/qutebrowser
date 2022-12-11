#!/usr/bin/lua
-- create, manage, and download playlists (for mpv)
--- supports www.youtube.com and odysee.com
--- uses .pls files
local posix = require('posix')

local playlist_dir = 'data/playlists/'

-- get the playlist from the current tab
local function get_playlist()
  local playlist = {}
return playlist end

-- save the current playlist
local function save_playlist(name)
  local playlist=get_playlist()
end

-- list all the playlists
local function list_playlists()
  local str={}
  for dir in io.popen('ls -pa '..playlist_dir..' | grep -v /'):lines() do
    str[#str+1] = dir:match('(.+)%..+')--"https://riptutorial.com/lua/example/20315/lua-pattern-matching"
  end
return str end

-- delete a playlist
local function delete_playlist(playlist)
end

local fifo = os.getenv('QUTE_FIFO')
--posix.setenv('QUTE_FIFO', 'message-info hello from yt_playlist.lua'..fifo)
io.popen('$QUTE_FIFO+="message-info hello"')

