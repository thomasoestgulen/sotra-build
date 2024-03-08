'''__main__.py'''

from sotra import setup_parser
from sotra import bridge
from sotra import obs


def main():
    parser = setup_parser.parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return
    
    if args.command == "obs":
        print(args)
        if args.list:
            obs.obs_to_txt(dest=args.dest,
                           obs=[*args.list])
        if args.cwd:
            current_obs = obs.obs_from_cwd()
            obs.obs_to_txt(dest=args.dest,
                           obs=current_obs)
    
    if args.command == "archive":
        obs.archive(src_dir=args.src,
                    obs=args.obs,
                    date=args.date)
    
    if args.command == "build":
        if args.bro:
            name = ""
            if args.name: 
                name = args.name
            bridge.build(name)
        elif args.name:
            bridge.name(args.name)


if __name__ == "__main__":
    main()
