#!/usr/bin/lua
-- create, manage, and download playlists|video queues (for mpv)
--- supports www.youtube.com and odysee.com
--- uses .pls files
local posix = require('posix')

local pl_dir = 'data/playlists/'-- the playlists dir


-- get the queue from the current tab
local function get_queue()
  local pl = {}-- the playlist
return pl end


-- convert playlist to pls format
local function get_playlist()
  local pl = {}-- the playlist
return pl end


-- save the current playlist to a pls file
local function save_playlist(name, playlist)
  local file = pl_dir .. name .. ".pls"
  local contents = "[playlist]\n"--save the file contents
end


-- list all the playlists
local function list_playlists(separator)
  local pls={}
  for dir in io.popen('ls -pa '..pl_dir..' | grep -v /'):lines() do
    pls[#pls+1] = dir:match('(.+)%..+')--"https://riptutorial.com/lua/example/20315/lua-pattern-matching"
  end

  local sep=separator or ', '
  local str=''
  for i,v in ipairs(pls) do
    str=str..sep..v
  end
return str end


-- delete a playlist
local function delete_playlist(playlist)
end





local fifo = os.getenv('QUTE_FIFO')
--posix.setenv('QUTE_FIFO', 'message-info hello from yt_playlist.lua'..fifo)
io.popen('QUTE_FIFO="message-info pl_dir = '..pl_dir..'"')

